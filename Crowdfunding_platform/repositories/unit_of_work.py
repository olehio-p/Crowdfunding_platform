from abc import ABC, abstractmethod
from django.db import transaction

from Crowdfunding_platform.repositories.category_repository import CategoryRepository
from Crowdfunding_platform.repositories.comment_repository import CommentRepository
from Crowdfunding_platform.repositories.custom_user_repository import CustomUserRepository
from Crowdfunding_platform.repositories.dispute_repository import DisputeRepository
from Crowdfunding_platform.repositories.donation_repository import DonationRepository
from Crowdfunding_platform.repositories.follower_repository import FollowerRepository
from Crowdfunding_platform.repositories.language_repository import LanguageRepository
from Crowdfunding_platform.repositories.location_repository import LocationRepository
from Crowdfunding_platform.repositories.milestone_repository import MilestoneRepository
from Crowdfunding_platform.repositories.payment_gateway_repository import PaymentGatewayRepository
from Crowdfunding_platform.repositories.project_repository import ProjectRepository
from Crowdfunding_platform.repositories.report_repository import ReportRepository
from Crowdfunding_platform.repositories.transaction_repository import TransactionRepository
from Crowdfunding_platform.repositories.update_repository import UpdateRepository


class AbstractUnitOfWork(ABC):
    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, *args):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass


class DjangoUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.projects = ProjectRepository()
        self.custom_users = CustomUserRepository()
        self.transactions = TransactionRepository()
        self.donations = DonationRepository()
        self.categories = CategoryRepository()
        self.comments = CommentRepository()
        self.disputes = DisputeRepository()
        self.followers = FollowerRepository()
        self.languages = LanguageRepository()
        self.locations = LocationRepository()
        self.milestones = MilestoneRepository()
        self.payment_gateways = PaymentGatewayRepository()
        self.reports = ReportRepository()
        self.updates = UpdateRepository()

    def __enter__(self):
        transaction.set_autocommit(False)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.rollback()
        else:
            self.commit()
        transaction.set_autocommit(True)

    def commit(self):
        transaction.commit()

    def rollback(self):
        transaction.rollback()
