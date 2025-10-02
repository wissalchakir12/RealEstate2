from agno.tools import tool
from typing import Dict, Any, List, Optional
import numpy as np
from datetime import datetime, timedelta


@tool(
    name="risk_assessment_engine",
    description="Comprehensive risk assessment for real estate investments",
    show_result=True,
)
def risk_assessment_engine(
    property_address: str,
    property_value: float,
    risk_categories: List[str] = ["market", "environmental", "financial", "legal"],
    assessment_horizon: int = 10,
) -> Dict[str, Any]:
    """
    Comprehensive risk assessment for real estate investments.
    
    Args:
        property_address: Address of the property
        property_value: Current property value
        risk_categories: Categories to assess (market, environmental, financial, legal)
        assessment_horizon: Assessment period in years
        
    Returns:
        Dictionary containing comprehensive risk assessment
    """
    current_date = datetime.now()
    
    # Risk assessment framework
    risk_assessments = {}
    
    if "market" in risk_categories:
        market_risks = {
            "price_volatility": {
                "probability": np.random.uniform(0.3, 0.7),
                "impact": np.random.uniform(0.1, 0.3),
                "description": "Property value fluctuations due to market conditions",
                "mitigation": "Diversify portfolio, monitor market trends"
            },
            "liquidity_risk": {
                "probability": np.random.uniform(0.2, 0.5),
                "impact": np.random.uniform(0.15, 0.4),
                "description": "Difficulty selling property quickly at fair market value",
                "mitigation": "Maintain cash reserves, price competitively"
            },
            "interest_rate_risk": {
                "probability": np.random.uniform(0.4, 0.8),
                "impact": np.random.uniform(0.1, 0.25),
                "description": "Impact of changing interest rates on property values",
                "mitigation": "Fixed-rate financing, rate hedging strategies"
            }
        }
        risk_assessments["market"] = market_risks
    
    if "environmental" in risk_categories:
        environmental_risks = {
            "flood_risk": {
                "probability": np.random.uniform(0.1, 0.4),
                "impact": np.random.uniform(0.2, 0.8),
                "description": "Property damage from flooding events",
                "mitigation": "Flood insurance, elevation certificates, drainage improvements"
            },
            "climate_change": {
                "probability": np.random.uniform(0.6, 0.9),
                "impact": np.random.uniform(0.1, 0.4),
                "description": "Long-term climate impacts on property value",
                "mitigation": "Energy efficiency upgrades, sustainable features"
            }
        }
        risk_assessments["environmental"] = environmental_risks
    
    if "financial" in risk_categories:
        financial_risks = {
            "cash_flow_risk": {
                "probability": np.random.uniform(0.3, 0.6),
                "impact": np.random.uniform(0.2, 0.5),
                "description": "Rental income shortfalls or vacancy periods",
                "mitigation": "Tenant screening, lease guarantees, reserve funds"
            },
            "credit_risk": {
                "probability": np.random.uniform(0.2, 0.4),
                "impact": np.random.uniform(0.3, 0.7),
                "description": "Financing difficulties or rate increases",
                "mitigation": "Strong credit profile, multiple lender relationships"
            }
        }
        risk_assessments["financial"] = financial_risks
    
    if "legal" in risk_categories:
        legal_risks = {
            "regulatory_changes": {
                "probability": np.random.uniform(0.4, 0.7),
                "impact": np.random.uniform(0.1, 0.4),
                "description": "New regulations affecting property use or value",
                "mitigation": "Stay informed on regulations, legal compliance"
            },
            "title_issues": {
                "probability": np.random.uniform(0.1, 0.3),
                "impact": np.random.uniform(0.5, 0.9),
                "description": "Title defects or ownership disputes",
                "mitigation": "Title insurance, thorough title search"
            }
        }
        risk_assessments["legal"] = legal_risks
    
    # Calculate overall risk metrics
    all_risks = []
    for category, risks in risk_assessments.items():
        for risk_name, risk_data in risks.items():
            risk_score = risk_data["probability"] * risk_data["impact"]
            all_risks.append({
                "category": category,
                "risk_name": risk_name,
                "probability": risk_data["probability"],
                "impact": risk_data["impact"],
                "risk_score": risk_score,
                "description": risk_data["description"],
                "mitigation": risk_data["mitigation"]
            })
    
    # Sort risks by score
    all_risks.sort(key=lambda x: x["risk_score"], reverse=True)
    
    # Calculate category risk scores
    category_scores = {}
    for category in risk_categories:
        if category in risk_assessments:
            category_risks = [risk for risk in all_risks if risk["category"] == category]
            avg_score = sum(risk["risk_score"] for risk in category_risks) / len(category_risks)
            category_scores[category] = round(avg_score, 3)
    
    # Overall risk assessment
    overall_risk_score = sum(category_scores.values()) / len(category_scores)
    risk_level = "Low" if overall_risk_score < 0.3 else "Medium" if overall_risk_score < 0.6 else "High"
    
    # Risk-adjusted value calculation
    risk_discount = overall_risk_score * 0.2  # Max 20% discount for high risk
    risk_adjusted_value = property_value * (1 - risk_discount)
    
    return {
        "property_info": {
            "address": property_address,
            "current_value": property_value,
            "assessment_date": current_date.isoformat(),
            "assessment_horizon": assessment_horizon
        },
        "risk_assessment": {
            "overall_risk_score": round(overall_risk_score, 3),
            "risk_level": risk_level,
            "category_scores": category_scores,
            "top_risks": all_risks[:5],  # Top 5 risks
            "risk_adjusted_value": round(risk_adjusted_value, 2),
            "value_at_risk": round(property_value - risk_adjusted_value, 2)
        },
        "detailed_risks": risk_assessments,
        "mitigation_strategy": {
            "immediate_actions": [risk["mitigation"] for risk in all_risks[:3]],
            "monitoring_requirements": [
                "Regular market analysis",
                "Environmental monitoring",
                "Financial performance tracking",
                "Legal compliance reviews"
            ]
        },
        "recommendations": {
            "investment_decision": "Proceed with caution" if risk_level == "High" else "Acceptable risk" if risk_level == "Medium" else "Low risk investment",
            "risk_management": "Implement comprehensive risk management plan"
        }
    }


@tool(
    name="demographic_analyzer",
    description="Analyze demographic trends and population characteristics",
    show_result=True,
)
def demographic_analyzer(
    location: str,
    analysis_radius: float = 1.0,
    demographic_categories: List[str] = ["population", "income", "education", "employment"],
    trend_period: int = 5,
) -> Dict[str, Any]:
    """
    Analyze demographic trends and population characteristics.
    
    Args:
        location: Geographic location (address, city, zip code)
        analysis_radius: Analysis radius in miles
        demographic_categories: Categories to analyze
        trend_period: Period for trend analysis in years
        
    Returns:
        Dictionary containing demographic analysis
    """
    current_date = datetime.now()
    
    # Simulated demographic data
    demographic_data = {}
    
    if "population" in demographic_categories:
        population_data = {
            "total_population": np.random.randint(15000, 100000),
            "population_density": np.random.randint(1000, 8000),
            "age_distribution": {
                "under_18": np.random.uniform(15, 25),
                "18_34": np.random.uniform(20, 35),
                "35_54": np.random.uniform(25, 35),
                "55_plus": np.random.uniform(15, 30)
            },
            "household_size": round(np.random.uniform(2.1, 2.8), 1),
            "growth_rate": round(np.random.uniform(-0.5, 3.5), 2),
            "migration_pattern": np.random.choice(["Inbound", "Outbound", "Stable"])
        }
        demographic_data["population"] = population_data
    
    if "income" in demographic_categories:
        income_data = {
            "median_household_income": np.random.randint(45000, 120000),
            "per_capita_income": np.random.randint(25000, 65000),
            "income_distribution": {
                "under_25k": np.random.uniform(10, 25),
                "25k_50k": np.random.uniform(15, 30),
                "50k_75k": np.random.uniform(20, 30),
                "75k_100k": np.random.uniform(15, 25),
                "over_100k": np.random.uniform(10, 30)
            },
            "income_growth_rate": round(np.random.uniform(1.0, 4.0), 2),
            "poverty_rate": round(np.random.uniform(5, 20), 1)
        }
        demographic_data["income"] = income_data
    
    if "education" in demographic_categories:
        education_data = {
            "high_school_graduation": round(np.random.uniform(80, 95), 1),
            "bachelor_degree": round(np.random.uniform(20, 60), 1),
            "advanced_degree": round(np.random.uniform(8, 25), 1),
            "school_quality_rating": np.random.randint(6, 10)
        }
        demographic_data["education"] = education_data
    
    if "employment" in demographic_categories:
        employment_data = {
            "unemployment_rate": round(np.random.uniform(2.5, 8.0), 1),
            "labor_force_participation": round(np.random.uniform(60, 75), 1),
            "job_growth_rate": round(np.random.uniform(0.5, 3.5), 2),
            "average_commute_time": np.random.randint(20, 45)
        }
        demographic_data["employment"] = employment_data
    
    # Calculate demographic score
    score_factors = []
    if "population" in demographic_data:
        score_factors.append(min(demographic_data["population"]["growth_rate"] / 3, 1))
    if "income" in demographic_data:
        score_factors.append(min(demographic_data["income"]["median_household_income"] / 100000, 1))
    if "education" in demographic_data:
        score_factors.append(demographic_data["education"]["bachelor_degree"] / 100)
    if "employment" in demographic_data:
        score_factors.append(1 - demographic_data["employment"]["unemployment_rate"] / 10)
    
    demographic_score = sum(score_factors) / len(score_factors) if score_factors else 0.5
    
    return {
        "location_info": {
            "location": location,
            "analysis_radius": analysis_radius,
            "analysis_date": current_date.isoformat(),
            "trend_period": trend_period
        },
        "demographic_data": demographic_data,
        "demographic_score": {
            "overall_score": round(demographic_score, 2),
            "rating": "Excellent" if demographic_score > 0.8 else "Good" if demographic_score > 0.6 else "Fair" if demographic_score > 0.4 else "Poor",
            "investment_attractiveness": "High" if demographic_score > 0.7 else "Medium" if demographic_score > 0.5 else "Low"
        },
        "recommendations": {
            "target_demographics": "Young professionals and families" if demographic_data.get("population", {}).get("age_distribution", {}).get("18_34", 0) > 25 else "Retirees and empty nesters",
            "property_types": ["Single-family homes", "Condominiums"] if demographic_data.get("income", {}).get("median_household_income", 0) > 60000 else ["Apartments", "Starter homes"],
            "investment_strategy": "Growth-oriented" if demographic_score > 0.7 else "Value-oriented"
        }
    }


@tool(
    name="regulatory_compliance_checker",
    description="Check regulatory compliance and identify compliance requirements",
    show_result=True,
)
def regulatory_compliance_checker(
    property_address: str,
    property_type: str = "residential",
    compliance_areas: List[str] = ["zoning", "building_codes", "environmental", "safety"],
    jurisdiction: str = "local",
) -> Dict[str, Any]:
    """
    Check regulatory compliance and identify compliance requirements.
    
    Args:
        property_address: Address of the property
        property_type: Type of property (residential, commercial, industrial)
        compliance_areas: Areas to check for compliance
        jurisdiction: Jurisdiction level (local, state, federal)
        
    Returns:
        Dictionary containing compliance assessment
    """
    current_date = datetime.now()
    
    # Simulated compliance database
    compliance_results = {}
    
    if "zoning" in compliance_areas:
        zoning_compliance = {
            "current_zoning": np.random.choice(["R1", "R2", "R3", "C1", "C2", "M1"]),
            "permitted_uses": [
                "Single-family residential",
                "Home office",
                "Accessory dwelling unit"
            ],
            "restrictions": [
                "Maximum height: 35 feet",
                "Minimum setback: 25 feet front, 10 feet side",
                "Maximum lot coverage: 40%"
            ],
            "compliance_status": np.random.choice(["Compliant", "Non-Compliant", "Conditional"]),
            "required_permits": ["Building permit", "Occupancy permit"],
            "recent_changes": "Zoning ordinance updated 2023-06-15"
        }
        compliance_results["zoning"] = zoning_compliance
    
    if "building_codes" in compliance_areas:
        building_compliance = {
            "applicable_codes": [
                "International Building Code 2021",
                "International Residential Code 2021",
                "Local amendments"
            ],
            "compliance_status": np.random.choice(["Compliant", "Partially Compliant", "Non-Compliant"]),
            "code_violations": [
                {"violation": "Electrical panel not up to code", "severity": "Medium", "deadline": "2024-06-01"},
                {"violation": "Missing smoke detectors", "severity": "High", "deadline": "2024-03-15"}
            ],
            "required_inspections": ["Electrical", "Plumbing", "HVAC", "Final"],
            "permit_status": "Active permits: 2, Expired permits: 0"
        }
        compliance_results["building_codes"] = building_compliance
    
    if "environmental" in compliance_areas:
        environmental_compliance = {
            "environmental_assessments": {
                "phase_1_esa": "Completed 2023-08-15",
                "phase_2_esa": "Not required",
                "asbestos_survey": "Completed 2023-07-20",
                "lead_paint_assessment": "Required for pre-1978 construction"
            },
            "compliance_status": "Compliant",
            "environmental_concerns": [
                "Former gas station within 500 feet",
                "Wetlands buffer zone restrictions"
            ],
            "required_permits": ["Stormwater permit", "Wetlands permit"],
            "monitoring_requirements": "Annual groundwater monitoring"
        }
        compliance_results["environmental"] = environmental_compliance
    
    if "safety" in compliance_areas:
        safety_compliance = {
            "fire_safety": {
                "sprinkler_system": "Required for commercial use",
                "fire_exits": "Compliant",
                "fire_alarm_system": "Installed and tested",
                "last_inspection": "2023-12-01"
            },
            "accessibility": {
                "ada_compliance": "Partially compliant",
                "required_modifications": ["Ramp installation", "Bathroom modifications"],
                "compliance_deadline": "2024-12-31"
            },
            "compliance_status": "Mostly Compliant"
        }
        compliance_results["safety"] = safety_compliance
    
    # Calculate overall compliance score
    compliance_scores = []
    for area, data in compliance_results.items():
        status = data.get("compliance_status", "Unknown")
        if status == "Compliant":
            compliance_scores.append(1.0)
        elif status in ["Partially Compliant", "Mostly Compliant", "Conditional"]:
            compliance_scores.append(0.7)
        elif status == "Non-Compliant":
            compliance_scores.append(0.3)
        else:
            compliance_scores.append(0.5)
    
    overall_compliance_score = sum(compliance_scores) / len(compliance_scores) if compliance_scores else 0.5
    
    return {
        "property_info": {
            "address": property_address,
            "property_type": property_type,
            "jurisdiction": jurisdiction,
            "assessment_date": current_date.isoformat()
        },
        "compliance_assessment": {
            "overall_compliance_score": round(overall_compliance_score, 2),
            "compliance_rating": "Excellent" if overall_compliance_score > 0.9 else "Good" if overall_compliance_score > 0.7 else "Fair" if overall_compliance_score > 0.5 else "Poor",
            "areas_assessed": compliance_areas,
            "detailed_results": compliance_results
        },
        "recommendations": {
            "immediate_actions": ["Address high-priority violations", "Update permits"],
            "professional_consultation": [
                "Zoning attorney for complex zoning issues",
                "Building code consultant for code compliance",
                "Environmental consultant for environmental issues"
            ],
            "monitoring_schedule": "Quarterly compliance reviews recommended"
        }
    }


@tool(
    name="investment_analyzer",
    description="Comprehensive investment analysis for real estate properties",
    show_result=True,
)
def investment_analyzer(
    property_value: float,
    investment_type: str = "buy_hold",
    financing_details: Optional[Dict[str, Any]] = None,
    market_assumptions: Optional[Dict[str, Any]] = None,
    analysis_period: int = 10,
) -> Dict[str, Any]:
    """
    Comprehensive investment analysis for real estate properties.
    
    Args:
        property_value: Current property value
        investment_type: Type of investment (buy_hold, fix_flip, rental, commercial)
        financing_details: Financing parameters
        market_assumptions: Market growth and rental assumptions
        analysis_period: Analysis period in years
        
    Returns:
        Dictionary containing comprehensive investment analysis
    """
    current_date = datetime.now()
    
    # Default parameters
    if financing_details is None:
        financing_details = {
            "down_payment_percent": 0.20,
            "interest_rate": 0.065,
            "loan_term_years": 30,
            "closing_costs_percent": 0.03
        }
    
    if market_assumptions is None:
        market_assumptions = {
            "annual_appreciation": 0.035,
            "rental_yield": 0.08,
            "rental_growth": 0.03,
            "vacancy_rate": 0.05,
            "expense_ratio": 0.35
        }
    
    # Calculate initial investment
    down_payment = property_value * financing_details["down_payment_percent"]
    closing_costs = property_value * financing_details["closing_costs_percent"]
    initial_investment = down_payment + closing_costs
    
    # Calculate loan details
    loan_amount = property_value - down_payment
    monthly_rate = financing_details["interest_rate"] / 12
    num_payments = financing_details["loan_term_years"] * 12
    
    if monthly_rate > 0:
        monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)
    else:
        monthly_payment = loan_amount / num_payments
    
    # Investment analysis
    annual_rental_income = property_value * market_assumptions["rental_yield"]
    effective_rental_income = annual_rental_income * (1 - market_assumptions["vacancy_rate"])
    annual_expenses = effective_rental_income * market_assumptions["expense_ratio"]
    annual_debt_service = monthly_payment * 12
    
    # Calculate returns
    annual_cash_flow = effective_rental_income - annual_expenses - annual_debt_service
    cash_on_cash_return = annual_cash_flow / initial_investment
    
    # Property appreciation
    final_property_value = property_value * (1 + market_assumptions["annual_appreciation"]) ** analysis_period
    total_appreciation = final_property_value - property_value
    
    # Total return calculation
    total_cash_flow = annual_cash_flow * analysis_period
    total_return = total_cash_flow + total_appreciation
    total_roi = total_return / initial_investment
    annualized_return = (1 + total_roi) ** (1/analysis_period) - 1
    
    return {
        "investment_info": {
            "property_value": property_value,
            "investment_type": investment_type,
            "analysis_period": analysis_period,
            "analysis_date": current_date.isoformat()
        },
        "investment_metrics": {
            "initial_investment": round(initial_investment, 2),
            "annual_cash_flow": round(annual_cash_flow, 2),
            "cash_on_cash_return": round(cash_on_cash_return * 100, 2),
            "total_return": round(total_return, 2),
            "total_roi": round(total_roi * 100, 2),
            "annualized_return": round(annualized_return * 100, 2),
            "final_property_value": round(final_property_value, 2)
        },
        "assumptions": {
            "financing": financing_details,
            "market": market_assumptions
        },
        "recommendations": {
            "investment_decision": "Proceed" if cash_on_cash_return > 0.06 else "Reconsider",
            "optimization_suggestions": [
                "Negotiate better purchase price",
                "Explore alternative financing options",
                "Consider different exit strategies"
            ]
        }
    }


@tool(
    name="neighborhood_profiler",
    description="Create comprehensive neighborhood profiles and amenity analysis",
    show_result=True,
)
def neighborhood_profiler(
    location: str,
    profile_categories: List[str] = ["amenities", "transportation", "schools", "safety", "lifestyle"],
    radius_miles: float = 1.0,
) -> Dict[str, Any]:
    """
    Create comprehensive neighborhood profiles and amenity analysis.
    
    Args:
        location: Geographic location (address, neighborhood, zip code)
        profile_categories: Categories to profile
        radius_miles: Analysis radius in miles
        
    Returns:
        Dictionary containing comprehensive neighborhood profile
    """
    current_date = datetime.now()
    
    # Simulated neighborhood data
    neighborhood_profile = {}
    
    if "amenities" in profile_categories:
        amenities_data = {
            "shopping": {
                "grocery_stores": np.random.randint(2, 8),
                "shopping_centers": np.random.randint(1, 4),
                "restaurants": np.random.randint(10, 50),
                "pharmacies": np.random.randint(1, 5),
                "banks": np.random.randint(2, 8)
            },
            "recreation": {
                "parks": np.random.randint(3, 12),
                "playgrounds": np.random.randint(2, 8),
                "sports_facilities": np.random.randint(1, 5),
                "fitness_centers": np.random.randint(2, 10),
                "libraries": np.random.randint(1, 3)
            },
            "healthcare": {
                "hospitals": np.random.randint(1, 3),
                "urgent_care": np.random.randint(1, 4),
                "medical_offices": np.random.randint(5, 20)
            },
            "amenity_score": round(np.random.uniform(6.5, 9.5), 1)
        }
        neighborhood_profile["amenities"] = amenities_data
    
    if "transportation" in profile_categories:
        transportation_data = {
            "public_transit": {
                "bus_stops": np.random.randint(3, 15),
                "subway_stations": np.random.randint(0, 3),
                "transit_score": np.random.randint(40, 95)
            },
            "walkability": {
                "walk_score": np.random.randint(50, 95),
                "bike_score": np.random.randint(40, 85),
                "pedestrian_friendly": np.random.choice([True, False])
            },
            "highways_access": {
                "nearest_highway": f"{np.random.uniform(0.5, 5):.1f} miles",
                "airport_distance": f"{np.random.uniform(10, 45):.1f} miles",
                "traffic_level": np.random.choice(["Light", "Moderate", "Heavy"])
            }
        }
        neighborhood_profile["transportation"] = transportation_data
    
    if "schools" in profile_categories:
        schools_data = {
            "elementary_schools": {
                "count": np.random.randint(2, 6),
                "average_rating": round(np.random.uniform(6, 10), 1)
            },
            "middle_schools": {
                "count": np.random.randint(1, 3),
                "average_rating": round(np.random.uniform(6, 10), 1)
            },
            "high_schools": {
                "count": np.random.randint(1, 3),
                "average_rating": round(np.random.uniform(6, 10), 1),
                "graduation_rate": f"{np.random.randint(85, 98)}%"
            },
            "overall_school_rating": round(np.random.uniform(6, 10), 1)
        }
        neighborhood_profile["schools"] = schools_data
    
    if "safety" in profile_categories:
        safety_data = {
            "crime_statistics": {
                "overall_crime_rate": round(np.random.uniform(15, 45), 1),
                "violent_crime_rate": round(np.random.uniform(2, 8), 1),
                "property_crime_rate": round(np.random.uniform(10, 35), 1),
                "crime_trend": np.random.choice(["Decreasing", "Stable", "Increasing"])
            },
            "emergency_services": {
                "police_response_time": f"{np.random.randint(3, 12)} minutes",
                "fire_response_time": f"{np.random.randint(4, 10)} minutes"
            },
            "safety_score": round(np.random.uniform(6, 9.5), 1)
        }
        neighborhood_profile["safety"] = safety_data
    
    if "lifestyle" in profile_categories:
        lifestyle_data = {
            "community_character": {
                "neighborhood_type": np.random.choice(["Urban", "Suburban", "Rural"]),
                "architectural_style": np.random.choice(["Modern", "Traditional", "Mixed", "Historic"]),
                "age_of_homes": f"{np.random.randint(10, 60)} years average"
            },
            "entertainment": {
                "nightlife_options": np.random.randint(2, 20),
                "cultural_venues": np.random.randint(1, 8),
                "movie_theaters": np.random.randint(1, 4)
            },
            "environmental": {
                "air_quality_index": np.random.randint(25, 85),
                "noise_level": np.random.choice(["Low", "Moderate", "High"]),
                "green_space": f"{np.random.randint(15, 45)}% coverage"
            }
        }
        neighborhood_profile["lifestyle"] = lifestyle_data
    
    # Calculate overall neighborhood score
    category_scores = []
    if "amenities" in neighborhood_profile:
        category_scores.append(neighborhood_profile["amenities"]["amenity_score"] / 10)
    if "transportation" in neighborhood_profile:
        walk_score = neighborhood_profile["transportation"]["walkability"]["walk_score"] / 100
        transit_score = neighborhood_profile["transportation"]["public_transit"]["transit_score"] / 100
        category_scores.append((walk_score + transit_score) / 2)
    if "schools" in neighborhood_profile:
        category_scores.append(neighborhood_profile["schools"]["overall_school_rating"] / 10)
    if "safety" in neighborhood_profile:
        category_scores.append(neighborhood_profile["safety"]["safety_score"] / 10)
    if "lifestyle" in neighborhood_profile:
        air_quality_score = (100 - neighborhood_profile["lifestyle"]["environmental"]["air_quality_index"]) / 100
        category_scores.append(air_quality_score)
    
    overall_score = sum(category_scores) / len(category_scores) if category_scores else 0.5
    
    return {
        "location_info": {
            "location": location,
            "analysis_radius": radius_miles,
            "profile_date": current_date.isoformat(),
            "categories_analyzed": profile_categories
        },
        "neighborhood_profile": neighborhood_profile,
        "overall_assessment": {
            "neighborhood_score": round(overall_score, 2),
            "rating": "Excellent" if overall_score > 0.8 else "Good" if overall_score > 0.6 else "Fair" if overall_score > 0.4 else "Poor",
            "investment_grade": "A" if overall_score > 0.8 else "B" if overall_score > 0.6 else "C" if overall_score > 0.4 else "D"
        },
        "investment_recommendations": [
            "Premium location suitable for high-end properties" if overall_score > 0.8 else "Good location with solid investment potential",
            "Target families with school-age children" if "schools" in neighborhood_profile and neighborhood_profile["schools"]["overall_school_rating"] > 8 else "Appeal to young professionals"
        ],
        "future_outlook": {
            "development_plans": "Mixed-use development planned for 2025-2027",
            "market_trend": "Stable to improving" if overall_score > 0.6 else "Stable",
            "investment_timing": "Good time to invest" if overall_score > 0.7 else "Monitor for opportunities"
        }
    }


@tool(
    name="economic_indicator_tracker",
    description="Track and analyze economic indicators affecting real estate markets",
    show_result=True,
)
def economic_indicator_tracker(
    location: str = "national",
    indicators: List[str] = ["interest_rates", "employment", "inflation", "gdp", "housing_market"],
    time_period: int = 12,
) -> Dict[str, Any]:
    """
    Track and analyze economic indicators affecting real estate markets.
    
    Args:
        location: Geographic scope (national, state, metro, local)
        indicators: Economic indicators to track
        time_period: Time period for analysis in months
        
    Returns:
        Dictionary containing economic indicator analysis
    """
    current_date = datetime.now()
    
    # Simulated economic data
    indicator_data = {}
    
    if "interest_rates" in indicators:
        base_rate = 5.25
        rate_history = []
        for i in range(min(6, time_period)):
            month_date = current_date - timedelta(days=30 * i)
            rate_change = np.random.uniform(-0.25, 0.25)
            rate = max(0.5, base_rate + rate_change * (i / time_period))
            rate_history.append({
                "date": month_date.strftime("%Y-%m"),
                "fed_funds_rate": round(rate, 2),
                "mortgage_30yr": round(rate + 1.5 + np.random.uniform(-0.2, 0.2), 2)
            })
        
        rate_trend = "Rising" if rate_history[0]["fed_funds_rate"] > rate_history[-1]["fed_funds_rate"] else "Falling"
        
        indicator_data["interest_rates"] = {
            "current_fed_funds": rate_history[0]["fed_funds_rate"],
            "current_30yr_mortgage": rate_history[0]["mortgage_30yr"],
            "trend": rate_trend,
            "12_month_change": round(rate_history[0]["fed_funds_rate"] - rate_history[-1]["fed_funds_rate"], 2),
            "forecast": "Rates expected to stabilize" if abs(rate_history[0]["fed_funds_rate"] - 5.0) < 0.5 else "Continued volatility expected",
            "historical_data": rate_history
        }
    
    if "employment" in indicators:
        employment_data = {
            "unemployment_rate": round(np.random.uniform(3.0, 6.5), 1),
            "job_growth_rate": round(np.random.uniform(0.5, 3.0), 1),
            "labor_force_participation": round(np.random.uniform(62, 67), 1),
            "wage_growth_rate": round(np.random.uniform(2.5, 5.0), 1),
            "employment_trend": np.random.choice(["Improving", "Stable", "Declining"])
        }
        indicator_data["employment"] = employment_data
    
    if "inflation" in indicators:
        inflation_data = {
            "cpi_annual": round(np.random.uniform(2.0, 4.5), 1),
            "core_cpi": round(np.random.uniform(2.5, 4.0), 1),
            "housing_inflation": round(np.random.uniform(3.0, 6.0), 1),
            "inflation_trend": np.random.choice(["Rising", "Falling", "Stable"]),
            "fed_target": 2.0
        }
        indicator_data["inflation"] = inflation_data
    
    if "gdp" in indicators:
        gdp_data = {
            "gdp_growth_annual": round(np.random.uniform(1.5, 4.0), 1),
            "gdp_growth_quarterly": round(np.random.uniform(0.3, 1.2), 1),
            "consumer_spending": round(np.random.uniform(2.0, 5.0), 1),
            "economic_phase": np.random.choice(["Expansion", "Peak", "Contraction", "Trough"]),
            "recession_probability": round(np.random.uniform(10, 35), 0)
        }
        indicator_data["gdp"] = gdp_data
    
    if "housing_market" in indicators:
        housing_data = {
            "home_price_index": round(np.random.uniform(280, 320), 1),
            "price_growth_annual": round(np.random.uniform(2.0, 8.0), 1),
            "existing_home_sales": round(np.random.uniform(4.0, 6.5), 1),
            "housing_starts": round(np.random.uniform(1200, 1600), 0),
            "months_supply": round(np.random.uniform(2.5, 6.0), 1),
            "affordability_index": round(np.random.uniform(100, 140), 0),
            "market_condition": "Seller's market" if np.random.uniform(2.5, 6.0) < 4.0 else "Buyer's market"
        }
        indicator_data["housing_market"] = housing_data
    
    # Calculate economic health score
    health_factors = []
    
    if "employment" in indicator_data:
        unemployment = indicator_data["employment"]["unemployment_rate"]
        health_factors.append(1 - (unemployment / 10))
    
    if "inflation" in indicator_data:
        inflation = indicator_data["inflation"]["cpi_annual"]
        health_factors.append(1 - abs(inflation - 2.5) / 5)
    
    if "gdp" in indicator_data:
        gdp_growth = indicator_data["gdp"]["gdp_growth_annual"]
        health_factors.append(min(gdp_growth / 4, 1))
    
    economic_health_score = sum(health_factors) / len(health_factors) if health_factors else 0.5
    
    # Real estate market implications
    market_implications = []
    
    if "interest_rates" in indicator_data:
        if indicator_data["interest_rates"]["current_30yr_mortgage"] > 7.0:
            market_implications.append("High mortgage rates may reduce buyer demand")
        elif indicator_data["interest_rates"]["current_30yr_mortgage"] < 5.0:
            market_implications.append("Low mortgage rates support buyer activity")
    
    if "employment" in indicator_data:
        if indicator_data["employment"]["unemployment_rate"] < 4.0:
            market_implications.append("Low unemployment supports housing demand")
    
    if "housing_market" in indicator_data:
        if indicator_data["housing_market"]["months_supply"] < 3.0:
            market_implications.append("Low inventory supports price appreciation")
    
    return {
        "analysis_info": {
            "location": location,
            "indicators_tracked": indicators,
            "time_period_months": time_period,
            "analysis_date": current_date.isoformat()
        },
        "economic_indicators": indicator_data,
        "economic_assessment": {
            "health_score": round(economic_health_score, 2),
            "health_rating": "Strong" if economic_health_score > 0.7 else "Moderate" if economic_health_score > 0.5 else "Weak",
            "overall_trend": "Positive" if economic_health_score > 0.6 else "Neutral" if economic_health_score > 0.4 else "Negative"
        },
        "market_implications": market_implications,
        "investment_recommendations": [
            "Favorable economic conditions for real estate investment" if economic_health_score > 0.7 else "Mixed economic signals - proceed with caution"
        ],
        "forecast": {
            "6_month_outlook": "Economic conditions expected to remain stable" if economic_health_score > 0.6 else "Economic uncertainty expected to continue",
            "key_factors_to_watch": [
                "Federal Reserve policy decisions",
                "Employment trends",
                "Inflation trajectory",
                "Housing supply and demand balance"
            ]
        }
    }
