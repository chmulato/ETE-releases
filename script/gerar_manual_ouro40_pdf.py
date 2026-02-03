#!/usr/bin/env python3
"""
Gera o PDF do Manual de Iniciação — Ouro 4.0 (Laboratório Campo Largo).
Conteúdo estruturado: pilares, mindset, visionário, blueprint, nível 0, skill tree, oráculo, dedicatória.
Uso: python gerar_manual_ouro40_pdf.py [caminho_saida.pdf]
Requer: pip install reportlab
"""

import sys
from pathlib import Path

try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import cm
    from reportlab.platypus import (
        Paragraph,
        SimpleDocTemplate,
        Spacer,
        Preformatted,
        Table,
        TableStyle,
        PageBreak,
    )
except ImportError:
    print("Erro: reportlab não instalado. Execute: pip install reportlab")
    sys.exit(1)


def _spacer(height_cm=0.4):
    return Spacer(1, height_cm * cm)


def _build_styles(styles):
    """Estilos customizados para o manual."""
    styles.add(ParagraphStyle(
        name="ManualTitle",
        parent=styles["Heading1"],
        fontSize=20,
        spaceAfter=6,
        textColor=colors.HexColor("#1a1a1a"),
        alignment=1,  # center
    ))
    styles.add(ParagraphStyle(
        name="ManualSubtitle",
        parent=styles["Normal"],
        fontSize=12,
        spaceAfter=20,
        textColor=colors.HexColor("#444"),
        alignment=1,
    ))
    styles.add(ParagraphStyle(
        name="SectionTitle",
        parent=styles["Heading1"],
        fontSize=14,
        spaceBefore=14,
        spaceAfter=8,
        textColor=colors.HexColor("#2d3748"),
    ))
    styles.add(ParagraphStyle(
        name="SubSection",
        parent=styles["Heading2"],
        fontSize=11,
        spaceBefore=10,
        spaceAfter=6,
        textColor=colors.HexColor("#4a5568"),
    ))
    styles.add(ParagraphStyle(
        name="Tagline",
        parent=styles["Normal"],
        fontSize=9,
        spaceAfter=4,
        leftIndent=0,
        textColor=colors.HexColor("#718096"),
        fontName="Helvetica-Oblique",
    ))
    styles.add(ParagraphStyle(
        name="Blockquote",
        parent=styles["Normal"],
        fontSize=10,
        leftIndent=18,
        rightIndent=18,
        spaceBefore=8,
        spaceAfter=8,
        textColor=colors.HexColor("#4a5568"),
        fontName="Helvetica-Oblique",
        borderColor=colors.HexColor("#cbd5e0"),
        borderWidth=1,
        borderPadding=8,
        backColor=colors.HexColor("#f7fafc"),
    ))
    styles.add(ParagraphStyle(
        name="Small",
        parent=styles["Normal"],
        fontSize=8,
        textColor=colors.grey,
    ))
    styles.add(ParagraphStyle(
        name="ManualCode",
        fontName="Courier",
        fontSize=9,
        leading=11,
        leftIndent=12,
        rightIndent=12,
        backColor=colors.HexColor("#f1f5f9"),
        borderPadding=6,
        spaceAfter=8,
    ))
    return styles


def main():
    base = Path(__file__).resolve().parent
    # Saída padrão: docs/assets/pdf (portal ETE-releases); fallback script/web/assets/pdf
    out_dir = base.parent / "docs" / "assets" / "pdf"
    if not out_dir.exists():
        out_dir = base / "web" / "assets" / "pdf"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "Manual_Iniciacao_Ouro40.pdf"
    if len(sys.argv) > 1:
        out_path = Path(sys.argv[1]).resolve()

    doc = SimpleDocTemplate(
        str(out_path),
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=1.8 * cm,
        bottomMargin=1.8 * cm,
    )
    styles = getSampleStyleSheet()
    styles = _build_styles(styles)
    story = []

    # ---- Capa / Título ----
    story.append(Paragraph("Laboratório Campo Largo · Ouro 4.0", styles["ManualTitle"]))
    story.append(Paragraph("Manual de Iniciação", styles["ManualSubtitle"]))
    story.append(_spacer(0.6))
    intro = (
        "A terra vermelha que você pisa no Parque Newton Puppi esconde segredos químicos "
        "que o resto do mundo importa da China. <b>Você pode ser quem vai programar o refino disso.</b> "
        "Este manual organiza o caminho das pedras: IFPR, ETE e materiais."
    )
    story.append(Paragraph(intro, styles["Normal"]))
    story.append(_spacer(0.8))

    # ---- 1. Três pilares ----
    story.append(Paragraph("1. Três pilares — Código, Matéria, Futuro", styles["SectionTitle"]))
    pilares = [
        "<b>O Código.</b> Python não é só script: é a linguagem que liga termodinâmica (Kps, pH, precipitação) a decisões de investimento. Um simulador que você roda no IFPR hoje pode virar planta amanhã.",
        "<b>A Matéria.</b> Rochas e cerâmicas de Campo Largo fazem do município um laboratório a céu aberto. A herança mineral que a região carrega é o mesmo tipo de insumo que alimenta semicondutores e ímãs de neodímio — bilhões em mercado global.",
        "<b>O Futuro.</b> O IFPR é o lugar onde o código vira matéria física: onde você aprende a não só simular, mas a conectar engenharia de processos ao chão de fábrica e ao refino real.",
    ]
    for p in pilares:
        story.append(Paragraph(p, styles["Normal"]))
        story.append(_spacer(0.25))
    story.append(_spacer(0.5))

    # ---- 2. O mindset 2025/2026 ----
    story.append(Paragraph("2. O mindset 2025/2026 — Conhecimento técnico é o cheat code", styles["SectionTitle"]))
    topicos_mindset = [
        ("Soberania Digital vs. Atômica", "Quem controla o código controla o software. Quem controla as terras raras controla o hardware do planeta.", "Todo chip, toda bateria de Tesla, todo ímã de neodímio: depende de lantanídeos. A China domina a cadeia porque domina a matéria-prima. Aprender a refinar aqui é aprender a não depender de quem segura a torneira."),
        ("Ouro 4.0 & Economia Espacial", "O solo de Campo Largo é o mesmo tipo de jogo que a NASA e a SpaceX enxergam em asteroides.", "Lantanídeos na Terra = lantanídeos em rochas espaciais. Quem entende Kps, pH e precipitação seletiva aqui entende a geologia de outros mundos. O cara que domina o refino hoje está escrevendo o manual de quem vai minerar em Marte."),
        ("IA + Bancada de Lab", "O que levava 10 anos agora leva 10 dias. A IA é o copiloto; você ainda pilota.", "Ferramentas como o Cursor estão acelerando a descoberta de ligas e rotas de refino. Você usa IA para priorizar quais experimentos fazer. Quem junta código + química + IA vira o recurso escasso que as indústrias disputam."),
        ("Geopolítica de Quintal", "Campo Largo é estrategicamente mais importante que muitas capitais.", "Rochas, cerâmicas, tradição mineral. Quem domina o refino local não pede licença para sentar na mesa. Um jovem de 16 anos que entende terras raras + Python já fala a língua que CEOs e ministérios de mineração precisam."),
    ]
    for tit, tagline, texto in topicos_mindset:
        story.append(Paragraph(tit, styles["SubSection"]))
        story.append(Paragraph(tagline, styles["Tagline"]))
        story.append(Paragraph(texto, styles["Normal"]))
        story.append(_spacer(0.35))
    story.append(_spacer(0.5))

    # ---- 3. A Janela do Visionário ----
    story.append(Paragraph("3. A Janela do Visionário — O fim da tela, o início da matéria", styles["SectionTitle"]))
    story.append(Paragraph("O mundo saturou de aplicativos e softwares. A próxima fronteira de riqueza e inovação é a <b>Engenharia de Materiais impulsionada por IA</b>.", styles["Normal"]))
    story.append(_spacer(0.4))
    topicos_vision = [
        ("Engenharia de Prompt para a Natureza", "Não peça para a IA escrever um poema; peça para ela encontrar a rota química mais curta para isolar o Neodímio do solo de Campo Largo.", "O prompt certo vira protocolo de laboratório."),
        ("O Laboratório Automatizado", "Imagine rodar 1.000 simulações no projeto ETE antes de gastar um único grama de reagente no laboratório do IFPR. Isso é eficiência de nível 1 (Type 1 Civilization).", "Simulação em massa + validação pontual. O laboratório físico vira o lugar onde você confirma o que o código já previu."),
        ("Riqueza Geracional", "Sistemas de software depreciam; patentes de novos processos químicos e materiais avançados valem fortunas por décadas.", "Ouro 4.0 é sobre construir ativos reais."),
        ("A Ponte IFPR–Mundo", "O campus local é sua base de lançamentos. O código que você escreve em Campo Largo hoje é o padrão industrial que o mundo usará em 2030.", "IFPR não é ponto de chegada — é plataforma."),
    ]
    for tit, tagline, texto in topicos_vision:
        story.append(Paragraph(tit, styles["SubSection"]))
        story.append(Paragraph(tagline, styles["Tagline"]))
        story.append(Paragraph(texto, styles["Normal"]))
        story.append(_spacer(0.35))
    story.append(Paragraph("<b>Timeline do Futuro</b>", styles["SubSection"]))
    timeline = [
        "<b>2025</b> — Base: código + química no IFPR. Primeiros experimentos ETE. IA como copiloto.",
        "<b>2030</b> — Padrão: processos que você desenhou viram referência. Campo Largo no mapa global de materiais.",
        "<b>2040</b> — Legado: ativos reais, patentes, soberania. Quem começou em 2025 colhe a riqueza geracional.",
    ]
    for t in timeline:
        story.append(Paragraph(t, styles["Normal"]))
        story.append(_spacer(0.15))
    story.append(_spacer(0.3))
    manifesto = "Não construímos mais só telas. Construímos <b>matéria que importa</b>: rotas de refino, ligas, cerâmicas, processos que o mundo vai usar. Ouro 4.0 é o compromisso de quem escolhe o laboratório e a engenharia de materiais como fronteira — em Campo Largo, no IFPR, hoje."
    story.append(Paragraph(manifesto, styles["Blockquote"]))
    story.append(_spacer(0.6))

    # ---- 4. The Blueprint (tabela) ----
    story.append(Paragraph("4. The Blueprint — Equivalência de Poder", styles["SectionTitle"]))
    story.append(Paragraph("A grade curricular do IFPR vista como treinamento para a Jornada Marte.", styles["Normal"]))
    story.append(_spacer(0.35))
    data_blueprint = [
        ["Na Grade", "Na Realidade"],
        ["Química Inorgânica", "Extração de Lantanídeos e Neodímio"],
        ["Informática / Algoritmos", "Automação do Simulador ETE em Python"],
        ["Físico-Química", "Termodinâmica de Reatores para o Ouro 4.0"],
    ]
    t = Table(data_blueprint, colWidths=[5 * cm, 10 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e2e8f0")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#2d3748")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
        ("TOPPADDING", (0, 0), (-1, 0), 8),
        ("BACKGROUND", (0, 1), (-1, -1), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e0")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(t)
    story.append(_spacer(0.35))
    story.append(Paragraph("Nível: Técnico Integrado / Superior Tecnológico · Reconhecimento MEC · IFPR Campo Largo.", styles["Small"]))
    story.append(_spacer(0.6))

    # ---- 5. Nível 0: Iniciando o Sistema ----
    story.append(Paragraph("5. Nível 0: Iniciando o Sistema", styles["SectionTitle"]))
    story.append(Paragraph("Checklist de carreira (o roadmap):", styles["SubSection"]))
    checklist = [
        "Setup: Instalar VS Code + Extensão Python.",
        "Exploração: Visitar o laboratório de Química do IFPR Campo Largo.",
        "Contribuição: Enviar sugestões e feedback pelo Canal de Melhorias (portal Ouro 4.0).",
    ]
    for c in checklist:
        story.append(Paragraph(f"• {c}", styles["Normal"]))
    story.append(_spacer(0.4))
    story.append(Paragraph("Primeiro script — Massa de óxido a partir do volume de lixívia (lógica ETE):", styles["SubSection"]))
    code = """# ETE — Primeiro cálculo: massa de óxido a partir do volume de lixívia
volume_lixivia_m3 = 1.0   # m³ de solução lixiviada (PLS)
concentracao_oxido_g_L = 2.5  # g/L de óxido na lixívia

volume_L = volume_lixivia_m3 * 1000
massa_oxido_kg = (concentracao_oxido_g_L * volume_L) / 1000

print(f"Volume lixívia: {volume_lixivia_m3} m³")
print(f"Massa de óxido: {massa_oxido_kg:.3f} kg")"""
    story.append(Preformatted(code, styles["ManualCode"]))
    story.append(_spacer(0.5))

    # ---- 6. The Skill Tree ----
    story.append(Paragraph("6. The Skill Tree: Sua Progressão de Elite", styles["SectionTitle"]))
    skill_niveis = [
        ("Nível 1: Scripting & Scouting (O Básico)", [
            "Dominar Sintaxe Python (Variáveis e Loops).",
            "Entender a Tabela Periódica (Foco em Lantanídeos).",
            "Instalar o Ambiente de Desenvolvimento (VS Code + ETE Repo).",
        ]),
        ("Nível 2: Process Engineer (Intermediário)", [
            "Estequiometria Aplicada (Cálculo de rendimento de óxidos).",
            "Manipulação de JSON/CSV (Alimentar o simulador com dados reais).",
            "Prática de Laboratório: Testes de pH e Precipitação Seletiva.",
        ]),
        ("Nível 3: Deep Tech Architect (Avançado)", [
            "Engenharia de Prompt para Otimização Química.",
            "Análise de Viabilidade Econômica via Código.",
            "Contribuição Ativa: Enviar melhorias e insights pelo Canal de Melhorias do portal.",
        ]),
    ]
    for tit_nivel, itens in skill_niveis:
        story.append(Paragraph(tit_nivel, styles["SubSection"]))
        for i in itens:
            story.append(Paragraph(f"□ {i}", styles["Normal"]))
        story.append(_spacer(0.25))
    story.append(_spacer(0.4))

    # ---- 7. O Oráculo ----
    story.append(Paragraph("7. O Oráculo", styles["SectionTitle"]))
    story.append(Paragraph("E se a argila do bairro tal tivesse 2% mais de Lantânio? O Simulador ETE recalcula sua margem de lucro em milissegundos. Para dados de entrada (CSV, JSON) e integração: use o Canal de Melhorias no portal (WhatsApp, Telegram ou e-mail).", styles["Normal"]))
    story.append(_spacer(0.5))

    # ---- 8. Links e Referências ----
    story.append(Paragraph("8. Links e Referências", styles["SectionTitle"]))
    links = [
        "IFPR Campo Largo: https://campolargo.ifpr.edu.br/",
        "Portal Ouro 4.0 / ETE-releases: https://chmulato.github.io/ETE-releases/",
        "Canal de Melhorias (feedback): canal-feedback.html no portal.",
    ]
    for link in links:
        story.append(Paragraph(link, styles["Normal"]))
    story.append(_spacer(0.6))

    # ---- 9. Dedicatória ----
    story.append(Paragraph("Dedicatória", styles["SectionTitle"]))
    story.append(Paragraph(
        "Este laboratório digital e a visão do Ouro 4.0 são dedicados ao <b>Prof. Dr. Urivald Pawlowsky</b>, "
        "Professor Titular da <b>UFPR</b> e referência em Engenharia de Recursos Hídricos e Ambiental. "
        "Sua trajetória prova que a ciência de alto nível nasce da união entre o rigor técnico e a paixão pelo nosso território.",
        styles["Normal"],
    ))
    story.append(_spacer(0.3))
    citacao = "A engenharia não transforma apenas a matéria; ela garante a soberania e o futuro do nosso ambiente."
    story.append(Paragraph(citacao, styles["Blockquote"]))
    story.append(_spacer(0.4))
    desafio_ia = (
        "<b>Desafio para o jovem entusiasta:</b> vá até uma IA (ChatGPT, Cursor, Copilot, Claude, etc.) e pergunte: "
        "«Quem foi o Prof. Dr. Urivald Pawlowsky da UFPR?» Descubra a trajetória e o legado de quem inspira este projeto."
    )
    story.append(Paragraph(desafio_ia, styles["Normal"]))
    story.append(_spacer(0.2))
    story.append(Paragraph("Sugestão de pergunta para copiar e colar na IA: \"Quem foi o Prof. Dr. Urivald Pawlowsky, professor da UFPR?\"", styles["Small"]))

    doc.build(story)
    print(f"PDF gerado: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
