from agno.knowledge.markdown import MarkdownKnowledgeBase
from agno.agent import Agent
from agno.team.team import Team
from agno.models.mistral import MistralChat
from agno.tools.file import FileTools
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.calculator import CalculatorTools
from agno.tools.python import PythonTools
from agno.storage.sqlite import SqliteStorage
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from dotenv import load_dotenv
import os
from pathlib import Path

# -------------------------------
# Import custom tools (au même niveau que module1.py)
# -------------------------------
from tools import (
    legal_document_analyzer,
    financial_calculator,
)
from additional_tools import (
    risk_assessment_engine,
    demographic_analyzer,
    regulatory_compliance_checker,
    investment_analyzer,
    neighborhood_profiler,
    economic_indicator_tracker
)

load_dotenv()

# -------------------------------
# Knowledge Base (SQLite only)
# -------------------------------
knowledge_base = None
try:
    knowledge_base = MarkdownKnowledgeBase(
        path=os.path.join(
            os.path.dirname(__file__),
            "knowledge",
            "Property_Valuation_Knowledge.md",
        ),
    )
    knowledge_base.load(recreate=False)
    print("✅ Knowledge base loaded with SQLite")
except Exception as e:
    print(f"⚠️ Warning: Could not load knowledge base: {e}")
    knowledge_base = None

# -------------------------------
# Shared storage and memory
# -------------------------------
storage = SqliteStorage(
    table_name="property_valuation_sessions",
    db_file="tmp/property_valuation.db"
)
memory = Memory(
    model=MistralChat(id="mistral-large-latest"),
    db=SqliteMemoryDb(
        table_name="property_valuation_records",
        db_file="tmp/property_valuation.db"
    ),
    delete_memories=False,
    clear_memories=False,
)

# -------------------------------
# Agents definitions
# -------------------------------
FinancialAnalystAgent = Agent(
    name="Financial Analyst",
    agent_id="FinancialAnalystAgent",
    model=MistralChat(id="mistral-medium-latest", api_key=os.getenv("MISTRAL_API_KEY")),
    tools=[
        FileTools(base_dir=Path(os.path.join(os.path.dirname(__file__), "documents")),
                  save_files=True, read_files=True, search_files=True),
        GoogleSearchTools(),
        CalculatorTools(),
        PythonTools(),
        financial_calculator,
        investment_analyzer,
        economic_indicator_tracker
    ],
    description="An AI agent specialized in financial analysis and investment evaluation for real estate properties.",
    instructions="You are FinancialAnalystAgent. Provide ROI, NPV, IRR, cash flow projections, and investment recommendations.",
    markdown=True,
    memory=memory,
    show_tool_calls=True,
    knowledge=knowledge_base
)

LegalComplianceAgent = Agent(
    name="Legal Compliance Specialist",
    agent_id="LegalComplianceAgent",
    model=MistralChat(id="mistral-medium-latest", api_key=os.getenv("MISTRAL_API_KEY")),
    tools=[
        FileTools(base_dir=Path(os.path.join(os.path.dirname(__file__), "documents")),
                  save_files=True, read_files=True, search_files=True),
        GoogleSearchTools(),
        legal_document_analyzer,
        regulatory_compliance_checker
    ],
    description="An AI agent specialized in legal compliance, zoning laws, building codes, and risk assessment.",
    instructions="You are LegalComplianceAgent. Review legal docs, identify risks, and ensure regulatory compliance.",
    markdown=True,
    memory=memory,
    show_tool_calls=True,
    knowledge=knowledge_base
)

RiskAssessmentAgent = Agent(
    name="Risk Assessment Specialist",
    agent_id="RiskAssessmentAgent",
    model=MistralChat(id="mistral-medium-latest", api_key=os.getenv("MISTRAL_API_KEY")),
    tools=[
        FileTools(base_dir=Path(os.path.join(os.path.dirname(__file__), "documents")),
                  save_files=True, read_files=True, search_files=True),
        GoogleSearchTools(),
        CalculatorTools(),
        PythonTools(),
        risk_assessment_engine,
        economic_indicator_tracker
    ],
    description="An AI agent specialized in market, environmental, and financial risk analysis.",
    instructions="You are RiskAssessmentAgent. Evaluate risks, probabilities, and propose mitigation strategies.",
    markdown=True,
    memory=memory,
    show_tool_calls=True,
    knowledge=knowledge_base
)

NeighborhoodSpecialistAgent = Agent(
    name="Neighborhood Specialist",
    agent_id="NeighborhoodSpecialistAgent",
    model=MistralChat(id="mistral-medium-latest", api_key=os.getenv("MISTRAL_API_KEY")),
    tools=[
        FileTools(base_dir=Path(os.path.join(os.path.dirname(__file__), "documents")),
                  save_files=True, read_files=True, search_files=True),
        GoogleSearchTools(),
        demographic_analyzer,
        neighborhood_profiler,
        economic_indicator_tracker
    ],
    description="An AI agent specialized in demographic analysis, community profiling, and amenities evaluation.",
    instructions="You are NeighborhoodSpecialistAgent. Analyze demographics, infrastructure, and location-based value drivers.",
    markdown=True,
    memory=memory,
    show_tool_calls=True,
    knowledge=knowledge_base
)

# -------------------------------
# Property Valuation Team
# -------------------------------
PropertyValuationTeam = Team(
    name="Property Valuation Team",
    model=MistralChat(id="mistral-medium-latest", api_key=os.getenv("MISTRAL_API_KEY")),
    members=[FinancialAnalystAgent, LegalComplianceAgent, RiskAssessmentAgent, NeighborhoodSpecialistAgent],
    description="A comprehensive team of AI agents specialized in advanced property valuation.",
    instructions="The Property Valuation Team collaborates across financial, legal, risk, and neighborhood expertise.",
    markdown=True,
    storage=storage,
    show_tool_calls=True,
    knowledge=knowledge_base
)

# -------------------------------
# Helper: filter only user-friendly report
# -------------------------------
def pretty_output(response):
    text = response.content
    if "###" in text:
        text = text[text.index("###"):]
    return text.strip()

# -------------------------------
# Tests agents réalistes (scénario investisseur)
# -------------------------------
def test_financial_analysis():
    print("\n🧪 Testing FinancialAnalystAgent...")
    question = """I am considering buying a property worth $500,000 
    with expected monthly rental income of $3,000. 
    I can finance it with a 20% down payment. 
    Please calculate ROI, NPV, IRR, and cash flow projections."""
    print(f"\n--- Question ---\n{question}\n")
    response = FinancialAnalystAgent.run(question)
    print("--- Agent Report ---")
    print(pretty_output(response))

def test_legal_compliance():
    print("\n🧪 Testing LegalComplianceAgent...")
    question = """Review the legal compliance for converting a commercial 
    property into residential apartments in downtown. 
    Check zoning laws, building codes, environmental rules, 
    and permits required. Identify risks."""
    print(f"\n--- Question ---\n{question}\n")
    response = LegalComplianceAgent.run(question)
    print("--- Agent Report ---")
    print(pretty_output(response))

def test_risk_assessment():
    print("\n🧪 Testing RiskAssessmentAgent...")
    question = """Conduct a full risk assessment for a waterfront villa investment. 
    Consider market risks, flooding/climate risks, financing risks, 
    and insurance needs. Provide mitigation strategies."""
    print(f"\n--- Question ---\n{question}\n")
    response = RiskAssessmentAgent.run(question)
    print("--- Agent Report ---")
    print(pretty_output(response))

def test_neighborhood_analysis():
    print("\n🧪 Testing NeighborhoodSpecialistAgent...")
    question = """Analyze the neighborhood of ziraoui. and say where ziraoui is located (city and country).
    Provide demographics, community profile, amenities, 
    infrastructure, and upcoming development projects."""
    print(f"\n--- Question ---\n{question}\n")
    response = NeighborhoodSpecialistAgent.run(question)
    print("--- Agent Report ---")
    print(pretty_output(response))

def test_comprehensive_valuation():
    print("\n🧪 Testing PropertyValuationTeam...")
    response = PropertyValuationTeam.run(
        message="""Conduct a comprehensive property valuation:
        1. Perform financial analysis
        2. Review legal compliance
        3. Assess risks
        4. Analyze neighborhood
        5. Provide a risk-adjusted final valuation report"""
    )
    print("--- Final Valuation Report ---")
    print(pretty_output(response))

# -------------------------------
# Main runner (si lancé en console)
# -------------------------------
if __name__ == "__main__":
    print("🏠 Property Valuation Module Loaded Successfully!")
    print("=" * 70)
    print("Agents: FinancialAnalystAgent, LegalComplianceAgent, RiskAssessmentAgent, NeighborhoodSpecialistAgent")
    print("Team: PropertyValuationTeam")
    print("=" * 70)

    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        print("\n⚠️ WARNING: MISTRAL_API_KEY not set in .env")
    else:
        try:
            # Active le test que tu veux
            #test_financial_analysis()
            test_legal_compliance()
            # test_risk_assessment()
            # test_neighborhood_analysis()
            # test_comprehensive_valuation()

            print("\n✅ Module test completed successfully!")
        except Exception as e:
            print(f"\n❌ Error during testing: {e}")
