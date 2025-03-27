import streamlit as st
import numpy as np
import datetime
import math
from dateutil.relativedelta import relativedelta
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO

# --- 🎨 Correction de la sidebar ---
st.markdown("""
    <style>
        /* Style des champs input pour un rendu plus élégant */
        section[data-testid="stSidebar"] input {
            color: #FFFFFF !important;  /* Texte blanc */
            background-color: #1E1E1E !important; /* Fond noir doux */
            font-size: 16px !important; /* Taille ajustée */
            font-weight: normal !important; /* Suppression du gras */
            border: none !important; /* Suppression des bordures internes */
            border-radius: 8px !important; /* Arrondir les coins */
            padding: 10px !important; /* Espacement interne */
            width: 100% !important; /* Champs bien remplis */
            outline: none !important; /* Supprimer la lueur autour du champ */
        }

        /* Style des boutons "+" et "-" pour les harmoniser */
        section[data-testid="stSidebar"] button {
            background-color: #1E1E1E !important; /* Même fond que les inputs */
            color: #FFFFFF !important; /* Texte en blanc */
            border: none !important; /* Supprimer les bordures */
            padding: 8px !important; /* Ajustement du padding */
            font-size: 16px !important; /* Taille homogène */
            border-radius: 8px !important; /* Bords arrondis */
        }
    </style>
""", unsafe_allow_html=True)



st.markdown("""
    <style>
        /* Fond de la sidebar */
        section[data-testid="stSidebar"] {
            background-color: #FFFFFF !important; /* Blanc */
        }

        /* Texte et labels dans la sidebar */
        section[data-testid="stSidebar"] * {
            color: #333333 !important; /* Noir foncé */
            font-weight: bold !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        /* 🎨 Garder la sidebar en blanc avec texte noir */
        section[data-testid="stSidebar"] {
            background-color: #FFFFFF !important; /* Fond blanc */
            color: #000000 !important; /* Texte noir */
        }

        /* 📝 Labels et textes en noir */
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] * {
            color: #000000 !important; /* Texte en noir */
            font-weight: normal !important;
        }

        /* 🔢 Style des champs input (fond noir, texte blanc) */
        section[data-testid="stSidebar"] input {
            color: #FFFFFF !important;  /* Texte blanc */
            background-color: #000000 !important; /* Fond noir */
            font-size: 16px !important; /* Taille ajustée */
            border: none !important; /* Pas de bordure interne */
            border-radius: 8px !important; /* Coins arrondis */
            padding: 12px !important; /* Espacement interne */
            width: 100% !important; /* Champs bien remplis */
            outline: none !important; /* Supprimer l'effet de focus */
        }

        /* ➕➖ Style des boutons "+" et "-" */
        section[data-testid="stSidebar"] button {
            background-color: #000000 !important; /* Même fond que les inputs */
            color: #FFFFFF !important; /* Texte blanc */
            border: none !important; /* Pas de bordure interne */
            padding: 8px !important; /* Ajustement du padding */
            font-size: 16px !important; /* Taille homogène */
            border-radius: 8px !important; /* Coins carrés */
            width: 40px !important; /* Largeur adaptée */
            height: 40px !important; /* Hauteur adaptée */
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
        }

        /* 🎯 Assurer que les icônes "+" et "-" restent bien visibles */
        section[data-testid="stSidebar"] button svg {
            fill: #FFFFFF !important; /* Icônes en blanc */
        }
    </style>
""", unsafe_allow_html=True)



# --- 📌 Formatage des nombres ---
def format_currency(value):
    """Formate les nombres en ajoutant un séparateur de milliers et une virgule comme séparateur décimal."""
    return f"{value:,.2f} €".replace(",", " ").replace(".", ",")



# --- 🎨 Correction du bandeau noir en Streamlit ---
st.markdown("""
    <style>
        .stSidebar, .css-1d391kg {
            background-color: #FFFFFF !important;
            color: #333333 !important;
        }
    </style>
""", unsafe_allow_html=True)



# --- 🎨 Personnalisation UI ---
st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
}
h1 {
    font-size: 3rem;
    font-weight: bold;
}
h3 {
    font-size: 1.8rem;
    font-weight: lighter;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        /* Réduit l'espace entre les paragraphes */
        p {
            margin-bottom: 2px !important;
        }
        /* Réduit l'espace sous les titres */
        h2, h3, h4 {
            margin-bottom: 5px !important;
        }
        /* Ajuste les éléments Streamlit */
        .stMarkdown {
            margin-bottom: 2px !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        /* Ajuste l'espace autour des titres */
        h2 {
            margin-top: 25px !important;  /* Plus d'espace avant */
            margin-bottom: 15px !important;  /* Plus d'espace après */
        }
        h3 {
            margin-top: 20px !important;
            margin-bottom: 10px !important;
        }
        h4 {
            margin-top: 18px !important;
            margin-bottom: 8px !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .contact-box {
            border: 2px solid #00A79D;  /* Bordure turquoise */
            padding: 15px;
            border-radius: 10px;
            background-color: rgba(0, 167, 157, 0.1); /* Légère transparence */
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            margin-top: 60px; /* Encore plus d'espace avant */
            margin-bottom: 60px; /* Encore plus d'espace après */
        }
        .contact-box a {
            color: #00A79D; /* Lien turquoise */
            text-decoration: none;
            font-weight: bold;
        }
        .contact-box a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)





# --- 🏠 Affichage du logo et du slogan ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("F:\OneDrive - TG FINANCE\Perso\Codes python\OptiRachatV2\logo.webp", width=300)


st.markdown("""
    <h2 style='text-align: center; color: #00A79D;'>
        Zéro complication, maxi économies
    </h2>
    <h3 style='text-align: center; color: #00A79D;'>
        Avec OptiRachat,<br> économiser n'a jamais été aussi simple !
    </h3>
""", unsafe_allow_html=True)

# --- Ajout de la ligne sous le slogan ---
st.markdown("""
    <h5 style='text-align: center; font-size: 1.2rem; color: black; margin-top : -15px; margin-bottom : +40px;'>
        Un outil pour simuler votre rachat de crédit
    </h5>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="
        width: 100%;
        height: 5px;
        background: linear-gradient(to right, rgba(0, 167, 157, 0), #00A79D, rgba(0, 167, 157, 0));
        border-radius: 5px;
        margin-top: -5px;
        margin-bottom: 15px;
    "></div>
""", unsafe_allow_html=True)


# --- 🎛 Paramètres du prêt ---
st.sidebar.header("Paramètres du prêt initial")
capital_initial = st.sidebar.number_input("Capital initial (€)", value=300000.0, step=1000.0)
original_rate = st.sidebar.number_input("Taux initial (% annuel)", value=3.0, step=0.1)
duration_months = st.sidebar.number_input("Durée initiale du prêt (en mois)", value=240, step=1)
start_date = st.sidebar.date_input("Date de départ du prêt actuel", value=datetime.date(2025, 3, 1))

today = datetime.date.today()
st.write(f"📅 **Date du jour :** {today.strftime('%d/%m/%Y')}")

# --- 📌 Fonctions de calcul ---
def calculate_remaining_principal(P, r_annual, N_months, n_months_elapsed):
    r = r_annual / 100 / 12
    numerator = (1 + r) ** N_months - (1 + r) ** n_months_elapsed
    denominator = (1 + r) ** N_months - 1
    return P * numerator / denominator

def calculate_monthly_payment(P, r_annual, N_months):
    r = r_annual / 100 / 12
    return P * r / (1 - (1 + r) ** (-N_months)) if r != 0 else P / N_months

# --- 📄 Fonction pour générer le PDF ---
def generate_pdf():
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    pdf.setTitle("OptiRachat - Simulation de Rachat de Prêt")

    # --- Mise en page ---
    width, height = A4
    y_position = height - 50  # Position initiale

    def add_line(text, size=12, bold=False, color=(0, 0, 0)):
        """Ajoute une ligne dans le PDF avec un style défini."""
        nonlocal y_position
        pdf.setFillColorRGB(*color)
        pdf.setFont("Helvetica-Bold" if bold else "Helvetica", size)
        pdf.drawString(50, y_position, text)
        y_position -= 20

    # --- Titre principal ---
    add_line("Simulation de Rachat de Prêt - OptiRachat", size=16, bold=True, color=(0, 0.5, 1))
    y_position -= 10  # Espace supplémentaire

    # --- Informations du prêt initial ---
    add_line("🏠 Situation actuelle du prêt", size=14, bold=True)
    add_line(f"Date initiale du prêt : {start_date.strftime('%d/%m/%Y')}")
    add_line(f"Capital restant dû : {format_currency(remaining_principal)}")
    add_line(f"Nombre de mensualités restantes : {n_remaining}")
    add_line(f"Mensualité actuelle : {format_currency(original_monthly)}")
    add_line(f"Coût total restant (sans rachat) : {format_currency(total_cost_original)}")
    y_position -= 10

    # --- Frais liés au rachat ---
    add_line("💰 Frais liés au rachat", size=14, bold=True)
    add_line(f"Pénalités de remboursement anticipé : {format_currency(penalty_interest)}")
    add_line(f"Garantie bancaire (1.5%) : {format_currency(guarantee_fee)}")
    add_line(f"Honoraires de courtage (1%) : {format_currency(brokerage_fee)}")
    add_line(f"Nouveau montant à financer : {format_currency(new_total)}")
    y_position -= 10

    # --- Comparaison avec le refinancement ---
    add_line("📉 Comparaison avec refinancement", size=14, bold=True)
    add_line(f"Taux proposé : {new_rate_input:.2f} %")
    add_line(f"Nouvelle mensualité : {format_currency(new_monthly_full)}")
    add_line(f"Coût total avec rachat : {format_currency(total_cost_refinanced)}")
    add_line(f"Gains nets (économie réalisée) : {format_currency(gains_nets)}", bold=True, color=(0, 0.6, 0))
    y_position -= 10

    # --- Conserver la mensualité initiale et réduire la durée ---
    add_line("📆 Option : Conserver la mensualité actuelle", size=14, bold=True)
    add_line(f"Nouvelle durée : {new_duration_years} ans et {new_duration_remaining_months} mois")
    add_line(f"Nouveau coût total : {format_currency(total_cost_with_reduced_duration)}")
    add_line(f"Économies réalisées : {format_currency(savings_with_reduced_duration)}", bold=True, color=(0, 0.6, 0))
    y_position -= 10

    # --- Bonus mojitos 🍹 ---
    add_line("🍹 Moins de taux, plus de mojitos !", size=14, bold=True, color=(0, 0.5, 1))
    add_line(f"Nombre de mojitos offerts : {int(mojito_count)} 🏝️")
    add_line("📢 L’abus d’alcool est dangereux pour la santé, à consommer avec modération", size=10, bold=True, color=(0, 0.5, 1))

    # --- Finalisation du PDF ---
    pdf.save()
    buffer.seek(0)
    return buffer

# --- 📊 Calcul des coûts et frais ---
N_total = int(duration_months)
n_elapsed = (today.year - start_date.year) * 12 + (today.month - start_date.month)
n_remaining = N_total - n_elapsed

remaining_principal = calculate_remaining_principal(capital_initial, original_rate, N_total, n_elapsed)
original_monthly = calculate_monthly_payment(capital_initial, original_rate, N_total)
total_cost_original = original_monthly * n_remaining

penalty_interest = min(6 * (remaining_principal * (original_rate / 100 / 12)), remaining_principal * 0.03)
guarantee_fee = (remaining_principal + penalty_interest) * 0.015
brokerage_fee = (remaining_principal + penalty_interest + guarantee_fee) * 0.01
total_fees = penalty_interest + guarantee_fee + brokerage_fee
new_total = remaining_principal + total_fees

# --- 🏦 Simulation de refinancement ---
new_rate_input = st.sidebar.number_input("Taux de refinancement proposé (% annuel)", value=1.0, step=0.1)
new_monthly_full = calculate_monthly_payment(new_total, new_rate_input, n_remaining)
total_cost_refinanced = new_monthly_full * n_remaining

# --- 💰 Calcul des gains nets ---
gains_nets = (total_cost_original - total_cost_refinanced) - total_fees

# --- 🎯 Calcul du taux de refinancement minimum ---
def binary_search_break_even(new_total, n_months_remaining, target_total_cost, low=0.0, high=10.0, tol=1e-6):
    while high - low > tol:
        mid = (low + high) / 2
        cost = calculate_monthly_payment(new_total, mid, n_months_remaining) * n_months_remaining
        if cost > target_total_cost:
            high = mid
        else:
            low = mid
    return (low + high) / 2

break_even_rate = binary_search_break_even(new_total, n_remaining, total_cost_original)



# --- 🎯 Calcul du point mort ---
monthly_saving_proposed = original_monthly - new_monthly_full
if monthly_saving_proposed > 0:
    break_even_months = math.ceil(total_fees / monthly_saving_proposed)
    if break_even_months > n_remaining or break_even_months > 600:
        break_even_date_str = "Point mort non atteint"
    else:
        break_even_date = today + relativedelta(months=break_even_months)
        break_even_date_str = break_even_date.strftime("%d/%m/%Y")
else:
    break_even_date_str = "Non applicable"

# --- 📉 Calcul de l'intérêt net du rachat ---
total_interest_original = total_cost_original - remaining_principal
total_interest_refinanced = total_cost_refinanced - remaining_principal
net_interest_savings = total_interest_original - total_interest_refinanced
net_total_savings = net_interest_savings - total_fees


# --- 📊 Affichage des résultats ---
st.subheader("🏠 Situation actuelle du prêt")
st.write(f"📅 **Date initiale du prêt :** {start_date.strftime('%d/%m/%Y')}")
st.write(f"📌 **Capital restant dû :** {format_currency(remaining_principal)}")
st.write(f"📌 **Nombre de mensualités restantes :** {n_remaining}")
st.write(f"📌 **Mensualité actuelle :** {format_currency(original_monthly)}")
st.write(f"📌 **Coût total restant (sans rachat) :** {format_currency(total_cost_original)}")

st.subheader("💰 Taux de refinancement minimum pour un rachat")
st.write(f"🎯 Le taux de refinancement doit être inférieur à **{break_even_rate:.4f}%** pour que le rachat soit intéressant.")

st.subheader("💰 Frais liés au rachat")
st.write(f"📌 **Capital restant dû :** {format_currency(remaining_principal)}")
st.write(f"➕ **Pénalités de remboursement anticipé :** {format_currency(penalty_interest)}")
st.write(f"➕ **Garantie bancaire (1.5%) :** {format_currency(guarantee_fee)}")
st.write(f"➕ **Honoraires de courtage (1%) :** {format_currency(brokerage_fee)}")
st.write(f"🟰 **Nouveau montant à financer :** {format_currency(new_total)}")



st.subheader("Comparaison sur la durée restante avec le nouveau taux")
st.write(f"**📊 Mensualité actuelle :** {format_currency(original_monthly)}")
st.write(f"**📊 Nouvelle mensualité avec rachat au taux de {new_rate_input:.2f}% :** {format_currency(new_monthly_full)}")
st.write(f"**📊 Coût total restant sans rachat :** {format_currency(total_cost_original)}")
st.write(f"**📊 Coût total restant avec rachat au taux de {new_rate_input:.2f}% :** {format_currency(total_cost_refinanced)}")
st.subheader("🎯 Date du point mort (frais absorbés)")
st.write(f"📆 **{break_even_date_str}**")


# Affichage dynamique des gains/pertes
color = "green" if gains_nets >= 0 else "red"
label = "💰 Gains nets ( frais absorbés ):" if gains_nets >= 0 else "💸 Pertes nettes :"
st.write(f"**{label}** <span style='color:{color}; font-weight:bold;'>{format_currency(gains_nets)}</span>", unsafe_allow_html=True)

# --- 🏦 OPTION : Conserver la mensualité actuelle et réduire la durée ---
st.subheader("📉 Conserver sa mensualité actuelle")

# Calcul du nombre de mois nécessaires pour rembourser le prêt avec la mensualité actuelle
def calculate_new_duration(P, r_annual, monthly_payment):
    r = r_annual / 100 / 12  # Taux mensuel
    if r == 0:  # Cas d'un taux à 0% (remboursement direct du capital)
        return math.ceil(P / monthly_payment)
    return math.ceil(math.log(1 / (1 - (P * r / monthly_payment))) / math.log(1 + r))

new_duration_months = calculate_new_duration(new_total, new_rate_input, original_monthly)

# Conversion en années et mois
new_duration_years = new_duration_months // 12
new_duration_remaining_months = new_duration_months % 12

# Calcul du coût total avec cette durée réduite
total_cost_with_reduced_duration = original_monthly * new_duration_months

# Économie réalisée par rapport au prêt initial
savings_with_reduced_duration = total_cost_original - total_cost_with_reduced_duration

st.write(f"📆 **Nouvelle durée du prêt si on conserve la mensualité actuelle :** {new_duration_years} ans et {new_duration_remaining_months} mois")
st.write(f"💰 **Nouveau coût total du prêt avec durée réduite :** {format_currency(total_cost_with_reduced_duration)}")

# Affichage dynamique des économies réalisées
color_savings = "green" if savings_with_reduced_duration >= 0 else "red"
label_savings = "💰 Économies réalisées :" if savings_with_reduced_duration >= 0 else "💸 Surcoût :"
st.write(f"**{label_savings}** <span style='color:{color_savings}; font-weight:bold;'>{format_currency(savings_with_reduced_duration)}</span>", unsafe_allow_html=True)

# --- 🍹 Bonus : Combien de mojitos avec les économies réalisées ? ---
mojito_price = 6.50
mojito_count = max(0, savings_with_reduced_duration // mojito_price)  # On évite d'afficher des mojitos négatifs !

st.write(f"🍹 **Moins de taux, plus de mojitos !** Avec ces économies, tu peux te payer **{mojito_count:,.0f} mojitos** ! Santé ! 🏝️😎".replace(",", " "))
st.markdown(
    "<p style='font-size: 12px; color: red; font-weight: bold;'>     📢 L’abus d’alcool est dangereux pour la santé, à consommer avec modération </p>", 
    unsafe_allow_html=True
)





st.subheader("📉 Synthèse")
st.write(f"💸 **Total intérêts restants avant le rachat :** {format_currency(total_interest_original)}")
st.write(f"💸 **Total intérêts après le rachat (frais déduits) :** {format_currency(total_interest_refinanced)}")
st.write(f"💰 **Différence intérêts entre les deux taux :** {format_currency(net_interest_savings)}")
st.write(f"💰 **Gains nets du rachat (après frais) :** {format_currency(net_total_savings)}")

st.subheader("📄 Télécharger votre simulation")

pdf_file = generate_pdf()
st.download_button(
    label="📥 Télécharger le PDF",
    data=pdf_file,
    file_name="OptiRachat_Simulation.pdf",
    mime="application/pdf"
)


st.markdown("""
    <style>
        .contact-box {
            border: 2px solid #00A79D;  /* Bordure turquoise */
            padding: 15px;
            border-radius: 10px;
            background-color: rgba(0, 167, 157, 0.1); /* Légère transparence */
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            margin-top: 60px; /* Encore plus d'espace avant */
            margin-bottom: 60px; /* Encore plus d'espace après */
        }
        .contact-box a {
            color: #00A79D; /* Lien turquoise */
            text-decoration: none;
            font-weight: bold;
        }
        .contact-box a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="contact-box">
        📩 Pour plus de renseignements, contactez-moi !<br><br>
        📨 DM via <a href="https://twitter.com/gusano197" target="_blank">@gusano197</a> ou ✉ <a href="mailto:nicolas.galan@talan-patrimoine.fr">contact@talan-patrimoine.fr</a>
    </div>
""", unsafe_allow_html=True)




# --- 🎨 Gestion du Mode Clair/Sombre + Amélioration de la visibilité ---
def set_theme():
    theme_css = '''
    <style>
        /* Fond clair par défaut */
        body, .stApp {
            background-color: #F8F9FA !important;
            color: #333333 !important;
        }

        /* Titres centrés */
        h2, h3 {
            text-align: center;
        }

        /* Sidebar en blanc */
        .stSidebar {
            background-color: #FFFFFF !important;
        }

        /* Style des inputs de la sidebar */
        section[data-testid="stSidebar"] input {
            color: #FFFFFF !important;  /* Chiffres en blanc */
            background-color: #000000 !important; /* Fond noir */
            font-size: 14px !important; /* Taille réduite */
            font-weight: normal !important; /* Suppression du gras */
            border: 1px solid #00A79D !important; /* Bordure verte */
            padding: 5px; /* Ajustement de l'espace interne */
        }

        /* Correction de la couleur des labels de la sidebar */
        section[data-testid="stSidebar"] label {
            color: #FFFFFF !important; /* Labels en blanc */
            font-size: 13px !important; /* Taille légèrement réduite */
            font-weight: normal !important; /* Suppression du gras */
        }
    </style>
    '''
    st.markdown(theme_css, unsafe_allow_html=True)

# Appliquer le thème
set_theme()



