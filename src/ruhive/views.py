from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"

class ProductsPage(generic.TemplateView):
    template_name = "products.html"

class ServicesPage(generic.TemplateView):
    template_name = "services.html"

class BlogPage(generic.TemplateView):
    template_name = "blog.html"

class ContactPage(generic.TemplateView):
    template_name = "contact.html"

class HadoopPage(generic.TemplateView):
    template_name = "hadoop.html"

class IOTPage(generic.TemplateView):
    template_name = "iot.html"

class DCPage(generic.TemplateView):
    template_name = "dc.html"
