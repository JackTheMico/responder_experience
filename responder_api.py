
import responder

description = "This is a sample server for Responder"
terms_of_service = "http://example.com/terms/"
contact = {
    "name": "API Support",
    "url": "http://www.example.com/support",
    "email": "support@example.com"
}
mylicense = {
    "name": "Apache 2.0",
    "url": "http://www.apache.org/license/LICENSE-2.0.html"
}

api = responder.API(
    title="Responder Demo Service",
    version="1.0",
    openapi="3.0.2",
    docs_route="/docs",
    description=description,
    terms_of_service=terms_of_service,
    contact=contact,
    license=mylicense
)
