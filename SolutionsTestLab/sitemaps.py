from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    i18n = True

    def items(self):
        return [
            "home",
            "about",
            "services",
            "quality_assurance",
            "software_testing",
            "test_management",
            "careers",
            "contact",
            "impressum",
            "privacy_policy",
            "blog",
            "blog_software_testing",
        ]

    def location(self, item):
        return reverse(item)