import concurrent.futures
import time
import random
from datetime import timedelta
from typing import List, Dict
from dataclasses import dataclass

from django.db.models import Count, Sum, Avg, F, Max, Min, Q
from django.db.models.functions import TruncMonth
from django.utils import timezone

from Crowdfunding_platform.models.project_models.Milestone import Milestone
from Crowdfunding_platform.models.project_models.Project import Project
from Crowdfunding_platform.models.project_models.Category import Category
from Crowdfunding_platform.models.user_models.CustomUser import CustomUser
from Crowdfunding_platform.models.transaction_models.Donation import Donation


@dataclass
class TestResult:
    workers: int
    batch_size: int
    total_time: float
    avg_query_time: float
    max_query_time: float
    min_query_time: float
    total_queries: int
    successful_queries: int
    failed_queries: int
    query_type: str


def generate_test_queries() -> Dict[str, List[callable]]:
    return {
        "simple_selects": [
            lambda: list(Project.objects.filter(status='active')),
            lambda: list(Category.objects.order_by('name')),
            lambda: list(CustomUser.objects.all()),
            lambda: list(Project.objects.values('title', 'goal_amount')),
        ],
        "complex_joins": [
            lambda: list(
                Project.objects.filter(status='active')
                .annotate(
                    category_name=F('category__name'),
                    donation_count=Count('donations'),
                    total_raised=Sum('donations__amount'),
                    milestone_count=Count('milestones')
                )
                .filter(total_raised__gt=10, milestone_count__gt=1)
                .order_by('-total_raised')
            ),
            lambda: list(
                Milestone.objects.select_related('project')
                .annotate(
                    backers_count=Count('project__donations', distinct=True),
                    total_milestone_raised=Sum('project__donations__amount'),
                    avg_donation=Avg('project__donations__amount')
                )
                .filter(Q(total_milestone_raised__gt=1000) | Q(backers_count__gt=50))
                .order_by('-total_milestone_raised')[:30]
            ),
        ],
        "advanced_aggregations": [
            lambda: list(
                Donation.objects.annotate(
                    month=TruncMonth('date')
                )
                .values('month')
                .annotate(
                    total_amount=Sum('amount'),
                    unique_donors=Count('user', distinct=True),
                    max_donation=Max('amount'),
                    min_donation=Min('amount')
                )
                .order_by('month')
            ),
            lambda: list(
                Project.objects.annotate(
                    unique_backers=Count('donations__user', distinct=True),
                    total_donations=Count('donations'),
                    total_amount=Sum('donations__amount'),
                    avg_donation=Avg('donations__amount'),
                    max_single_donation=Max('donations__amount'),
                    recent_donor_count=Count('donations',
                                             filter=Q(donations__date__gte=timezone.now() - timedelta(days=30)))
                )
                .filter(total_donations__gt=1)
                .order_by('-total_amount')
            )
        ],
        "very_hard_selects": [
            lambda: list(
                CustomUser.objects.annotate(
                    total_backed_projects=Count('donations__project', distinct=True),
                    total_donation_amount=Sum('donations__amount'),
                    backed_categories=Count('donations__project__category', distinct=True),
                    projects_over_threshold=Count(
                        'donations__project',
                        filter=Q(donations__project__current_amount__gt=F('donations__project__goal_amount')),
                        distinct=True
                    )
                )
                .filter(
                    Q(total_backed_projects__gt=1) &
                    Q(total_donation_amount__gt=10) &
                    Q(backed_categories__gt=2)
                )
                .order_by('-total_donation_amount')
            )
        ]
    }


def execute_query(query_callable):
    start_time = time.time()
    try:
        query_callable()
        execution_time = time.time() - start_time
        return execution_time
    except Exception as e:
        print(f"Query execution failed: {e}")
        return -1


def process_batch(queries: List[callable], worker_count: int) -> List[float]:
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=worker_count) as executor:
        future_to_query = {executor.submit(execute_query, query): query for query in queries}
        for future in concurrent.futures.as_completed(future_to_query):
            execution_time = future.result()
            if execution_time > 0:
                results.append(execution_time)
    return results


class CrowdfundingDatabaseTester:
    def __init__(self):
        self.queries = generate_test_queries()

    def run_performance_test(self, worker_counts: List[int], batch_sizes: List[int]) -> List[TestResult]:
        results = []

        for query_type, query_list in self.queries.items():
            for worker_count in worker_counts:
                for batch_size in batch_sizes:
                    print(f"Testing {query_type} with {worker_count} workers, batch size {batch_size}")
                    current_batch = random.sample(query_list, min(batch_size, len(query_list)))

                    start_time = time.time()
                    execution_results = process_batch(current_batch, worker_count)
                    total_time = time.time() - start_time

                    if execution_results:
                        results.append(
                            TestResult(
                                workers=worker_count,
                                batch_size=batch_size,
                                total_time=total_time,
                                avg_query_time=sum(execution_results) / len(execution_results),
                                max_query_time=max(execution_results),
                                min_query_time=min(execution_results),
                                total_queries=len(current_batch),
                                successful_queries=len(execution_results),
                                failed_queries=len(current_batch) - len(execution_results),
                                query_type=query_type
                            )
                        )

        return results


def run_crowdfunding_tests():
    worker_counts = [1, 2, 4, 8, 16, 32, 64, 128]
    batch_sizes = [10, 25, 50, 100, 200, 500, 1000, 5000]

    try:
        tester = CrowdfundingDatabaseTester()
        results = tester.run_performance_test(worker_counts, batch_sizes)
        return [vars(result) for result in results]
    except Exception as e:
        print(f"Test failed: {e}")
        return []