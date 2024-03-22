"""
File: tests/leads.py

For populating database with test leads, as well as sorting out bugs & issues. 

Author: Logan Lee

Still need to go through phone for pictures of people on the road. 
"""
from webmasterLee.models import Lead, LeadDiscoveryMethod

discovery_methods = [
    LeadDiscoveryMethod(
        method="Lansing Building Products", 
        method_description="Discovered from merch seen on people that came into Lansing."
    ),
    LeadDiscoveryMethod(
        method="Public Display",
        method_description="Car decals, business card bulletins, signs or other public display."
    ),
    LeadDiscoveryMethod(
        method="Family/Friend Referral",
        method_description="A family or friend referred them to me."
    ),
    LeadDiscoveryMethod(
        method="Client Referral",
        method_description="A client referred them to me."
    ),
    LeadDiscoveryMethod(
        method="Google Advertising",
        method_description="Found me through my google ads."
    ),
    LeadDiscoveryMethod(
        method="Facebook Advertising",
        method_description="Found me through my facebook ads."
    ),
]

# Leads listed concurrent with 17-March-2024
leads = [
    Lead(
        company="Harper Audio Productions", name="Roderick Harper",
        phone="5027241192", discovery_method_id=3,
        comment="Reffered through Callie, already has website but is unhappy I think... harperaudioproductions.com",
        ), 
    Lead(
        company="Bluegrass Gutters", phone="5029754526",
        discovery_method_id=1,
        ),
    Lead(
        company="Masden Concrete & Hauling", phone="5026485997",
        comment="Billy from Lansing's fathers company",
        discovery_method_id=1,
        ),
    Lead(
        company="Tipton Construction & Home Improvement", phone="3177174810",
        email="anthonytipton@gmail.com",
        discovery_method_id=1,
        ),
    Lead(
        company="Thrasher Improvements", phone="5028021437", name="Jason",
        discovery_method_id=1,
        ),
    Lead(
        company="SC General Contracting", phone="5023869308",
        discovery_method_id=1,
        ),
    Lead(
        company="a cut above rennovations".title(), phone="5027595335",
        discovery_method_id=1,
        ),
    Lead(
        company="heaton rennovations".title(), phone="5026403214",
        discovery_method_id=1,
        ),
    Lead(
        company="biard property".title(), phone="8126403214",
        discovery_method_id=1,
        ),
    Lead(
        company="kentuckiana siding".title(), phone="5022221953",
        discovery_method_id=1,
        ),
    Lead(
        company="JP One LLC", phone="5023807470",
        discovery_method_id=1,
        ),
    Lead(
        company="cracker jack construction".title(), phone="2709457859",
        discovery_method_id=1,
        ),
    Lead(
        company="traditional heating & cooling".title(), phone="5026439126",
        discovery_method_id=1,
        ),
    Lead(
        company="Defining Edge", phone="5028214299",
        discovery_method_id=1,
        ),
    Lead(
        company="502 Gutter Crew", phone="5022260536",
        comment="He is interested in cleaning windows for a small finders fee.",
        discovery_method_id=1,
        ),
    Lead(
        company="Handyman Services LLC", phone="5026578450",
        discovery_method_id=1,
        ),
    Lead(
        company="Ixma Roofing", phone="2702315651",
        discovery_method_id=1,
        ),
    Lead(
        company="Diaz Gutter Works", phone="5022206091",
        discovery_method_id=1,
        ),
    Lead(
        company="Precision Contracting", phone="5023383365",
        discovery_method_id=1,
        ),
    Lead(
        company="Bourbon Country Roofing", phone="5027698560",
        discovery_method_id=1,
        ),
    Lead(
        company="Hamilton Vinyl Siding", phone="5022490218",
        discovery_method_id=1,
        ),
    Lead(
        company="Mattingly Seamless", phone="2706991712",
        discovery_method_id=1,
        ),
    Lead(
        company="Froggies Bar & Grill", phone="5022524004",
        comment="Has Facebook page, need to work fast if I want this account",
        discovery_method_id=1,
        ),
    Lead(
        company="Seryel LLC", phone="5028077469",
        discovery_method_id=1,
        ),
    Lead(
        company="Future Services", phone="5023619470",
        discovery_method_id=2,
        ),
    Lead(
        company="Before & After Roofing", phone="5025510059",
        discovery_method_id=2,
        ),
    Lead(
        company="The Washboard", phone="5025431480",
        discovery_method_id=2,
        ),
    Lead(
        company="Kebs Tree Service", phone="5029557284",
        discovery_method_id=1,
        ),
    Lead(
        company="MoveAHaulics", phone="5029124277",
        discovery_method_id=2,
        ),
    Lead(
        company="RP Services LLC", phone="5029755148",
        discovery_method_id=2,
        ),
    Lead(
        company="Nue & Improved", phone="5023141997",
        discovery_method_id=2,
        ),
    Lead(
        company="FreeFlow Air Duct", phone="5025933636",
        comment="Could be a good connection for Greenleaf Cleaning",
        discovery_method_id=2,
        ),
    Lead(
        company="JBC Construction", phone="5023029740",
        discovery_method_id=2,
        ),
    Lead(
        company="Bill Ditsch-Gutter Delivery", phone="5022956831",
        discovery_method_id=1,
        ),
    Lead(
        company="Empire Home Improvement", phone="5029748386",
        discovery_method_id=2,
        ),
    Lead(
        company="Matherly Services (Cemetary)", phone="5022400353",
        comment="Cemetary design services.",
        discovery_method_id=2,
        ),
    Lead(
        company="Matherly Services", phone="5029122194",
        comment="Drain cleaning & faucet repair",
        discovery_method_id=2,
        ),
    Lead(
        company="Heating & Cooling", phone="5024091146",
        discovery_method_id=2,
        ),
    Lead(
        company="Berryman Roofing", phone="5029991300",discovery_method_id=2,
        ),
    Lead(
        company="Dr Housecare", phone="5023332283", discovery_method_id=2,
        ),
    Lead(
        company="E.B. Remodeling Services LLC", phone="5028819242", discovery_method_id=2,
        ),
    Lead(
        company="Bethel's Remodeling LLC", phone="5022998343", discovery_method_id=2,
        ),
    Lead(
        company="Kentucky Bluegrass Lawn Care & Property Management", phone="5026561143",
        discovery_method_id=2,
        ),
    Lead(
        company="American Concrete", phone="5023148945",
        discovery_method_id=2,
        ),
    Lead(
        company="Dicks Dryer Vent Cleaning", phone="2707822494",
        discovery_method_id=2,
        ),
    Lead(
        company="Integrity Auto Mobile Repairs", phone="5025538344",
        discovery_method_id=2,
        ),
    Lead(
        company="Glory Electric LLC", phone="8129878289",
        discovery_method_id=2,
        ),
    Lead(
        company="Artsy Avenue", phone="",
        comment="Check apple photos 23-may-2023",
        discovery_method_id=2,
        ),
    Lead(
        company="Kentuckiana Lawn & Landscaping", phone="5023773560",
        discovery_method_id=2,
        ),
    Lead(
        company="Kentuckiana Lawn Care", phone="8129724074",
        discovery_method_id=2,
        ),
    Lead(
        company="Roof Man", phone="5026510996",
        discovery_method_id=2,
        ),
    Lead(
        company="New Dream Rennovation", phone="5025516559",
        discovery_method_id=1,
    ),
]

from flask_sqlalchemy import SQLAlchemy

def populate_discovery_methods(db: SQLAlchemy, methods: list) -> None:
    # we love transactions <3
    with db.session.begin():
        for m in methods:
            db.session.add(m)
    # commit the transaction
    db.session.commit()

def populate_leads(db: SQLAlchemy, leads: list) -> None:
    # starting transaction
    with db.session.begin():
        for i in leads:
            db.session.add(i)
    # commit changes outside the context
    db.session.commit()

