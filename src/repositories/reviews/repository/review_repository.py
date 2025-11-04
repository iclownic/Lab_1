from typing import Dict, List
from common.models import Review
from common.interfaces import ReviewRepo

class SimpleReviewRepository(ReviewRepo):
    def __init__(self):
        self._reviews: Dict[str, Review] = {}
        self._product_reviews: Dict[str, List[str]] = {}  # product_id -> list of review_ids
    
    def get(self, review_id: str) -> Review:
        return self._reviews.get(review_id)
    
    def add(self, review: Review) -> None:
        self._reviews[review.id] = review
        # Додаємо до списку відгуків товару
        if review.product_id not in self._product_reviews:
            self._product_reviews[review.product_id] = []
        self._product_reviews[review.product_id].append(review.id)
    
    def update(self, review: Review) -> None:
        self._reviews[review.id] = review
    
    def list_for_product(self, product_id: str) -> List[Review]:
        # Отримати всі відгуки для товару
        review_ids = self._product_reviews.get(product_id, [])
        return [self._reviews[rid] for rid in review_ids if rid in self._reviews]