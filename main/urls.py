from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("services/quality-assurance/", views.quality_assurance, name="quality_assurance"),
    path("services/software-testing/", views.software_testing, name="software_testing"),
    path("services/test-management/", views.test_management, name="test_management"),
    path("careers/", views.careers, name="careers"),
    path("contact/", views.contact, name="contact"),

    path("impressum/", views.impressum, name="impressum"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path("blog/", views.blog, name="blog"),
    path("blog/software-testing/", views.blog_software_testing, name="blog_software_testing"),
]