from rest_framework.routers import DefaultRouter
from .views import LoanPredictionViewSet

router = DefaultRouter()
router.register(r'predict', LoanPredictionViewSet, basename='loan-predict')

urlpatterns = router.urls
