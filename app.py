import streamlit as st

# Configuración de página
st.set_page_config(
    page_title="Menú - El Chaquito de Felipe",
    page_icon="🥩",
    layout="centered"
)

# Inyección de CSS Avanzado para diseño web a medida de alta gama
st.markdown("""
    <style>
    /* Desactivar elementos nativos que dan aspecto de software */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Configuración de fondo y tipografía base */
    .stApp {
        background-color: #12100E; /* Carbón profundo premium */
        color: #EFECE6; /* Crema suave visualmente descansado */
        font-family: 'Playfair Display', 'Segoe UI', serif;
    }
    
    /* Diseño del Banner Principal de la marca */
    .brand-header {
        text-align: center;
        padding: 40px 10px 20px 10px;
        background: linear-gradient(180deg, #1C1917 0%, #12100E 100%);
        border-bottom: 2px solid #C2410C;
        margin-bottom: 30px;
        border-radius: 0 0 20px 20px;
    }
    .brand-title {
        font-size: 32px;
        font-weight: 800;
        color: #C2410C; /* Fuego Vivo */
        letter-spacing: 2px;
        margin: 0;
    }
    .brand-subtitle {
        font-size: 14px;
        color: #A19B93;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-top: 5px;
    }
    
    /* Estilización radical de las Pestañas (Tabs) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #1C1917;
        padding: 8px;
        border-radius: 12px;
        border-bottom: none;
        overflow-x: auto;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border: 1px solid #2D2824;
        border-radius: 8px;
        padding: 10px 16px;
        color: #A19B93;
        transition: all 0.3s ease;
    }
    .stTabs [aria-selected="true"] {
        background-color: #C2410C !important;
        color: #FFFFFF !important;
        border-color: #C2410C !important;
        font-weight: 600;
        box-shadow: 0 4px 12px rgba(194, 65, 12, 0.3);
    }

    /* Subtítulos de sección elegantes */
    .section-title {
        font-size: 22px;
        color: #C2410C;
        border-left: 3px solid #C2410C;
        padding-left: 12px;
        margin-top: 30px;
        margin-bottom: 20px;
        font-weight: 600;
    }
    
    /* Tarjetas de platos premium (Menu Cards) */
    .menu-card {
        background-color: #1C1917;
        border: 1px solid #2D2824;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        transition: transform 0.2s ease;
    }
    .menu-card:hover {
        border-color: #542207;
    }
    .menu-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 6px;
    }
    .menu-item-name {
        font-size: 18px;
        font-weight: 700;
        color: #FEFACC; /* Crema destacado */
    }
    .menu-item-price {
        font-size: 16px;
        font-weight: 700;
        color: #C2410C;
        background-color: rgba(194, 65, 12, 0.1);
        padding: 4px 12px;
        border-radius: 20px;
        border: 1px solid rgba(194, 65, 12, 0.2);
    }
    .menu-item-desc {
        font-size: 14px;
        color: #A19B93;
        line-height: 1.5;
    }
    
    /* Bloque informativo inferior */
    .premium-footer {
        text-align: center;
        background: #1C1917;
        border: 1px solid #2D2824;
        padding: 30px 20px;
        border-radius: 16px;
        margin-top: 5px;
    }
    .footer-info-row {
        font-size: 14px;
        color: #CBD5E1;
        margin-bottom: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Render de la cabecera estilizada de restaurante
st.markdown("""
    <div class="brand-header">
        <div class="brand-title">EL CHAQUITO DE FELIPE</div>
        <div class="brand-subtitle">Alta Parrilla & Maridaje</div>
    </div>
""", unsafe_allow_html=True)

# Sistema de pestañas premium
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🥩 Parrillas", 
    "🍽️ Especialidades", 
    "🍢 Platos y Piqueos", 
    "🥤 Bebidas",
    "🍷 Vinos"
])

# Función moldeadora para generar las tarjetas de menú elegantes de forma limpia
def render_plato(nombre, precio, descripcion=""):
    desc_html = f"<div class='menu-item-desc'>{descripcion}</div>" if descripcion else ""
    st.markdown(f"""
        <div class="menu-card">
            <div class="menu-header">
                <div class="menu-item-name">{nombre}</div>
                <div class="menu-item-price">{precio}</div>
            </div>
            {desc_html}
        </div>
    """, unsafe_allow_html=True)

with tab1:
    st.markdown('<div class="section-title">Parrillas Selectas a las Brasas</div>', unsafe_allow_html=True)
    st.caption("*Todas nuestras parrillas incluyen como acompañamiento tradicional: Arroz con queso o graneado, porción de papas fritas crujientes y ensalada fresca.")
    st.write("")
    
    render_plato("Parrilla Personal", "150 Bs.", "1 Unidad de Chorizo selecto, 150g de Vacío tierno, 100g de Chuleta de Cerdo, 50g de Asado de Tira, 50g de Filete de Pollo, Ubre y Tripitas crujientes.")
    render_plato("Parrilla Bi Personal", "190 Bs.", "2 Unidades de Chorizo selecto, 300g de Vacío tierno, 150g de Chuleta de Cerdo, 100g de Asado de Tira, 100g de Filete de Pollo, Ubre y Tripitas crujientes.")
    render_plato("Parrilla Tri Personal", "230 Bs.", "3 Unidades de Chorizo selecto, 500g de Vacío tierno, 300g de Chuleta de Cerdo, 200g de Asado de Tira, 200g de Filete de Pollo, Ubre y Tripitas crujientes.")

with tab2:
    st.markdown('<div class="section-title">Especialidades de la Casa</div>', unsafe_allow_html=True)
    render_plato("Bife de Chorizo", "90 Bs.", "150g de Bife de Chorizo premium. Servido con arroz con queso o graneado, papas fritas crocantes y ensalada selecta.")
    render_plato("Brocheta Chaquito", "90 Bs.", "80g de Churrasco premium intercalado con tripitas, ubre, filete de pollo, cebollas y morrones asados. Acompañado de arroz con queso, papas fritas y ensalada.")
    render_plato("Filete de Res", "100 Bs.", "150g de Filete tierno de res. Acompañado con arroz con queso o graneado, papas fritas y ensalada de la casa.")

    st.markdown('<div class="section-title">Cortes Individuales Chaquito</div>', unsafe_allow_html=True)
    render_plato("Corte Vacío (230g)", "60 Bs.", "Corte tierno tradicional acompañado con arroz con queso o graneado, papas fritas y ensalada fresca.")
    render_plato("Corte Pollo (200g)", "60 Bs.", "Filete jugoso a la parrilla acompañado con arroz con queso o graneado, papas fritas y ensalada fresca.")
    render_plato("Corte Cerdo (200g)", "60 Bs.", "Chuleta de cerdo seleccionada acompañada con arroz con queso o graneado, papas fritas y ensalada fresca.")
    render_plato("Medio Churrasco (110g)", "50 Bs.", "Porción ideal de churrasco acompañada con arroz con queso o graneado, papas fritas y ensalada fresca.")

with tab3:
    st.markdown('<div class="section-title">Platos Tradicionales</div>', unsafe_allow_html=True)
    render_plato("Chorizo al Plato", "60 Bs.", "3 Unidades de chorizo criollo de la casa, servidos con arroz con queso o graneado, papas fritas o yucas tiernas y ensalada.")
    render_plato("Pacumuto Entero", "60 Bs.", "100g de churrasco ensartado con chorizo tradicional, tripitas y ubre. Acompañado de arroz con queso o graneado, papas fritas y ensalada.")
    render_plato("Asado de Tira", "60 Bs.", "200g de tira delgada corte especial a la parrilla, arroz con queso o graneado, papas fritas o yucas y ensalada.")
    
    st.markdown('<div class="section-title">Piqueos para Compartir</div>', unsafe_allow_html=True)
    render_plato("Antojito", "40 Bs.", "1 Chorizo picado y 1 porción de vacío picado, acompañados de pan artesanal tostado a la parrilla y salsa chimichurri casera.")
    render_plato("Capricho", "60 Bs.", "1.5 chorizos picados, 2 porciones de vacío picado y 1 filete de pollo troceado. Servido con papas fritas, pan a la parrilla y salsa chimichurri.")
    render_plato("Al Límite", "80 Bs.", "Piqueo generoso de 2 chorizos picados, 3 porciones de vacío picado y 2 filetes de pollo troceados. Servido con papas fritas, pan a la parrilla y salsa chimichurri.")
    
    st.markdown('<div class="section-title">Opciones Express y Extras</div>', unsafe_allow_html=True)
    render_plato("Choripán de la Casa", "15 Bs.", "Chorizo criollo al carbón en pan crujiente con lechuga, tomate, papas al hilo y chimichurri.")
    render_plato("Guarniciones Extra", "15 Bs.", "Porción adicional a elección: Papas fritas, Arroz con queso o graneado, Filete de Pollo, Chuleta o Chorizo criollo.")
    render_plato("Ensalada Extra", "12 Bs.", "Porción de ensalada fresca de la casa.")

with tab4:
    st.markdown('<div class="section-title">Jugos Naturales</div>', unsafe_allow_html=True)
    render_plato("Jarra Grande (De Temporada)", "20 Bs.", "Ideal para compartir en la mesa.")
    render_plato("Jarra Mediana (De Temporada)", "15 Bs.", "Preparados al instante con fruta fresca.")
    render_plato("Vaso Personal / Frutal 1L", "5 Bs. / 15 Bs.", "Opciones individuales y botellas frutales.")
    
    st.markdown('<div class="section-title">Gaseosas y Cervezas</div>', unsafe_allow_html=True)
    render_plato("Línea de Gaseosas", "3 Bs. a 20 Bs.", "Disponibles en formatos: Personal 330ml (3 Bs.), 500ml (10 Bs.), 1 Litro (12 Bs.) y 2 Litros (20 Bs.).")
    render_plato("Cerveza Huari (620ml)", "25 Bs.", "Tradición cervecera de pureza excepcional.")
    render_plato("Cerveza Paceña (620ml)", "24 Bs.", "La cerveza insignia, helada y refrescante.")

with tab5:
    st.markdown('<div class="section-title">Vinos Clásicos del Sur</div>', unsafe_allow_html=True)
    st.caption("*Maridajes sugeridos para potenciar las notas de nuestras carnes a las brasas.")
    st.write("")
    render_plato("Kohlberg Clásico", "55 Bs.", "Variedades disponibles: Vino Tinto, Vino Blanco u Oporto de la tradicional bodega sureña.")
    render_plato("Campos de Solana Clásico", "55 Bs.", "Variedades disponibles: Vino Tinto, Vino Blanco u Oporto de alta consistencia.")
    render_plato("Stirpe Selección", "55 Bs.", "Variedades disponibles: Vino Tinto, Vino Blanco u Oporto.")

# Bloque final corporativo estilizado
st.markdown("---")
st.markdown("""
    <div class="premium-footer">
        <div class="footer-info-row"><b>📍 Ubicación:</b> Calle Panamá, casi esq. Plaza Uyuni (Miraflores), La Paz, Bolivia</div>
        <div class="footer-info-row"><b>📱 Pedidos & Reservas:</b> +591 68133991 &nbsp;|&nbsp; <b>🛵 Delivery:</b> Pedidos Ya</div>
        <div class="footer-info-row"><b>📸 Instagram / TikTok:</b> @Chaquito de Felipe</div>
        <p style="color: #C2410C; font-size: 16px; font-weight: bold; margin-top: 15px; letter-spacing: 1px;">LA MEJOR PARRILLA DE LA CIUDAD</p>
    </div>
""", unsafe_allow_html=True)
    
