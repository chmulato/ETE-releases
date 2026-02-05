# Changelog — chmulato/ETE

Todas as mudanças notáveis do ecossistema **chmulato/ETE** (Conhecimento Aberto + Ferramenta de Execução) são documentadas neste arquivo.

- **Formato:** [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).
- **Versionamento:** [Semantic Versioning](https://semver.org/lang/pt-BR/) para releases do instalador desktop.
- **Categorias de entrega:** [Web/Manifesto] | [Simulador/Engine] | [Legal/DPO] | [DevOps/Automação].

Cada versão inclui uma nota de **Impacto** para o jovem de Campo Largo e para a soberania tecnológica.

---

## [Unreleased]

### [Web/Manifesto]
- Nenhuma entrada pendente.

### [Simulador/Engine]

#### Adicionado
- Shell Electron opcional: aplicativo desktop alternativo ao pywebview.
- Modo `--flask-only`: sobe servidor Flask sem janela.

### [Legal/DPO]
- Nenhuma entrada pendente.

### [DevOps/Automação]

#### Adicionado
- Script de build local: gera instalador .exe com checksums.
- Testes E2E com Selenium: valida interface e regras de negócio.

#### Planejado
- Testes exaustivos do instalador .exe.

---

## [1.1.9] — 2026-01-26

### Impacto

| Público | Efeito |
|--------|--------|
| **Jovem de Campo Largo** | Interface unificada Ambiental ↔ Mineração; Termos de Uso acessíveis; clareza sobre inspiração e propriedade. |
| **Soberania tecnológica** | Cláusula de Salvaguarda de Legado; build local único. |

### [Simulador/Engine]

#### Adicionado
- Layout simbiótico: painel dividido Ambiental/Mineração com gradiente.
- Modal Desbloqueio de Protocolo Secreto: ativação por chave.
- Termos de Uso e Créditos: cláusula de Salvaguarda de Legado.

### [Legal/DPO]

#### Adicionado
- Cláusula de Salvaguarda de Legado: inspiração vs. propriedade.

### [DevOps/Automação]

#### Alterado
- Build local único: referências unificadas em script.

---

## [1.1.0] — 2026-01-26

### Impacto

| Público | Efeito |
|--------|--------|
| **Jovem de Campo Largo** | Primeiro delivery público: download .exe com checksums; canal de feedback. |
| **Soberania tecnológica** | Separação desenvolvimento/distribuição; integridade via checksums. |

### [DevOps/Automação]

#### Adicionado
- Primeiro delivery: workflow publica .exe e checksums nas Releases.
- Guia de delivery: checklist e comandos para tag/push.

### [Web/Manifesto]
- Portal e canal de feedback; link no simulador.

---

## [1.0.0] — 2025-01-26

### Impacto

| Público | Efeito |
|--------|--------|
| **Jovem de Campo Largo** | Manifesto web e simulador desktop gamificado; download .exe; badge de confiança. |
| **Soberania tecnológica** | Conhecimento e ferramenta desacoplados; pipeline CI valida matemática. |

### [Web/Manifesto]

#### Adicionado
- Laboratório Campo Largo: Ouro 4.0 com pilares, timeline, Skill Tree.
- Download Central: botão dinâmico para .exe, badge build.
- Manual PDF: gerado automaticamente.
- CSS/JS: tema escuro, persistência.

#### Alterado
- Dedicatória Pawlowsky: link removido.

### [Simulador/Engine]

#### Adicionado
- Aplicativo desktop Minerador 4.0: pywebview + Flask + engine Python.
- Fases: Guardião Ambiental e Alquimista de Metais.
- Licenciamento: validação chave, PIX.
- Biblioteca Digital: conteúdo pedagógico.
- Galeria Estratégica: cards de estudo.
- UI: estética Centro de Refino Espacial.

### [Legal/DPO]

#### Adicionado
- Canal feedback e LGPD: consentimento, triagem vulnerabilidades.
- Seção "Reportar Evolução" no simulador.

### [DevOps/Automação]

#### Adicionado
- Validação QA: PyTest para engine.
- Pipeline CI: testes + build .exe + release.
- Spec PyInstaller: configuração para .exe.

#### Corrigido
- Spec PyInstaller: ajuste variável SPECPATH.

---

## Como usar este changelog

- **[Unreleased]:** alterações planejadas ou em desenvolvimento.
- **[X.Y.Z]:** versão de release; para o instalador, use a tag `vX.Y.Z` no GitHub para disparar o release automático.
- **Impacto:** cada versão documenta o efeito para o jovem de Campo Largo e para a soberania tecnológica.

[Unreleased]: https://github.com/chmulato/ETE/compare/v1.1.9...HEAD  
[1.1.9]: https://github.com/chmulato/ETE/releases/tag/v1.1.9  
[1.1.0]: https://github.com/chmulato/ETE/releases/tag/v1.1.0  
[1.0.0]: https://github.com/chmulato/ETE/releases/tag/v1.0.0
