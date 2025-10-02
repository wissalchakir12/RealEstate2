import streamlit as st
import sys
from pathlib import Path
import markdown

# ------------------------------
# Ajouter le dossier modules au PYTHONPATH
# ------------------------------
sys.path.append(str(Path(__file__).parent / "modules" / "module1"))

# ------------------------------
# Importer le module1
# ------------------------------
modules = {}
try:
    import module1 as module1
    modules['module1'] = module1
except ImportError as e:
    st.error(f"Erreur d'importation du module: {e}")
    st.info("Assurez-vous que modules/module1/module1.py existe et contient PropertyValuationTeam")

# ------------------------------
# Config de la page
# ------------------------------
st.set_page_config(
    page_title="🏠 Property Valuation",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------------------
# Module info
# ------------------------------
MODULES = {
    "module1": {
        "name": "Property Valuation",
        "description": "Automated property assessment and market analysis",
        "icon": "🏠",
        "team": "Property Valuation Team",
    }
}

def get_module_team(module_name):
    """Retourne la team associée au module"""
    try:
        if module_name not in modules:
            return None
        module = modules[module_name]
        if hasattr(module, "PropertyValuationTeam"):
            return getattr(module, "PropertyValuationTeam")
        return None
    except Exception as e:
        st.error(f"Erreur lors du chargement de {module_name}: {e}")
        return None

def display_chat_message(message, is_user=True):
    """Affiche un message style chat"""
    html_message = markdown.markdown(message, extensions=['nl2br'])
    bubble_color = "#0ea5e9" if is_user else "#f3f4f6"
    text_color = "white" if is_user else "black"
    align = "right" if is_user else "left"

    st.markdown(
        f"""
        <div style="margin:8px 0; text-align:{align}">
            <div style="
                display:inline-block;
                background:{bubble_color};
                color:{text_color};
                padding:12px 16px;
                border-radius:16px;
                max-width:75%;
                word-wrap:break-word;
                font-size:15px;
                line-height:1.5;
            ">
                {html_message}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def chat_interface(module_name):
    """Interface de chat avec la team"""
    module_info = MODULES[module_name]
    st.markdown(
        f"""
        <h2>{module_info['icon']} {module_info['name']}</h2>
        <p>{module_info['description']}</p>
        <p><b>Team:</b> {module_info['team']}</p>
        """,
        unsafe_allow_html=True,
    )

    chat_key = f"{module_name}_chat"
    if chat_key not in st.session_state:
        st.session_state[chat_key] = []

    # Historique du chat
    for msg in st.session_state[chat_key]:
        display_chat_message(msg["content"], msg["is_user"])

    # ------------------------------
    # Input utilisateur style ChatGPT
    # ------------------------------
    prompt = st.chat_input("💬 Posez votre question...")
    if prompt:
        st.session_state[chat_key].append({"content": prompt, "is_user": True})
        display_chat_message(prompt, is_user=True)

        team = get_module_team(module_name)
        if team:
            with st.spinner("Analyse en cours..."):
                try:
                    response = team.run(prompt).content
                except Exception as e:
                    response = f"Erreur lors de l'appel à la team: {str(e)}"
        else:
            response = "⚠️ Team non disponible."

        st.session_state[chat_key].append({"content": response, "is_user": False})
        display_chat_message(response, is_user=False)

def main():
    with st.sidebar:
        st.title("Property OS")
        st.markdown("**Modules disponibles :**")
        if st.button("Property Valuation", use_container_width=True):
            st.session_state.current_module = "module1"
            st.rerun()

    if "current_module" not in st.session_state:
        st.session_state.current_module = "module1"

    if st.session_state.current_module:
        chat_interface(st.session_state.current_module)

if __name__ == "__main__":
    main()
