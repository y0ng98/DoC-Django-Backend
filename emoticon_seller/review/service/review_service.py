from abc import ABC, abstractmethod


class ReviewService(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def registerReview(self, reviewTitle, reviewWriter, reviewContent,reviewRating,reviewImage):
        pass

    @abstractmethod
    def readReview(self, reviewId):
        pass

    @abstractmethod
    def updateReview(self, reviewId, reviewData):
        pass

    @abstractmethod
    def removeReview(self, reviewId):
        pass