# Página Amazon + Campanha Google Ads — Diagnóstico e estado (11/10/2026)

## 1. De onde veio cada informação

| Fonte | Situação |
|---|---|
| Histórico do Claude Cowork (manifestos `manifest-*.json` neste repositório) | **Inacessível.** São só índices de uma exportação de dados do claude.ai. Os links valiam 24 h a partir de 08/10/2026 e, além de expirados, são bloqueados por verificação de navegador. **Não li as conversas do Cowork.** |
| Google Drive → `06 - SITE, CONTEÚDO E MARKETING` | **Lido.** É de lá que vem tudo o que está abaixo. |
| Pasta `06 …/novo` (06/10/2026, 19:15–19:16) | Versão **mais recente** das 3 páginas. Foi a usada aqui. |
| Pasta `06 …` raiz (06/10/2026, 11:26) | Versão anterior das mesmas 3 páginas. Mantida no Drive, não usada. |

Consequência: as decisões abaixo foram **inferidas dos arquivos**, não do histórico da conversa. Se no Cowork ficou combinado algo que não aparece nos arquivos (orçamento, domínio, ID de conversão, ajustes pedidos e ainda não feitos), isso não está refletido aqui.

## 2. Objetivo (inferido)

Captar vendedores com conta desativada ou saldo retido na Amazon, usando como prova de autoridade o processo nº 0815621-50.2025.8.15.2001 (TJPB, 3ª Câmara Cível, decisão definitiva em 05/10/2026). O tráfego viria do Google Ads e cairia numa página que leva ao WhatsApp.

## 3. O que está concluído

| Entrega | Arquivo | Estado |
|---|---|---|
| Landing page principal | `site/defesa-vendedor.html` | Pronta: hero, notificações reais, linha do tempo, 6 fundamentos com trecho do acórdão, Amazon.com/EUA, checklist de documentos, "quando o resultado pode ser diferente", FAQ, avaliações do Google, rodapé com Provimento 205/2021. |
| Página do caso completo | `site/caso-real.html` | Pronta. |
| Página de contato | `site/contato-vendedor.html` | Pronta. O formulário monta a mensagem e abre o WhatsApp (sem servidor, sem armazenar dados). |
| Evento de conversão no código | as 3 páginas | `whatsapp_click` dispara em todo botão `data-cta` e no formulário. |
| Base de palavras-chave | Drive: "Relatório de geração de páginas SEO — Amazon Seller" | 50 slugs/temas. |

As 3 páginas foram copiadas **byte a byte** do Drive para `site/`, **sem nenhuma alteração** (SHA-256 no commit).

Conferências feitas no texto: **nenhum nome de cliente** e **nenhum valor de condenação** aparecem; os trechos das notificações têm o nome das lojas omitido; a página tem uma seção honesta sobre decisões desfavoráveis e o aviso "o resultado de um processo não garante o mesmo resultado em outro".

## 4. O que fiz nesta sessão

- `google-ads/CAMPANHA.md`: estrutura completa (configuração, 5 grupos, extensões, medição, importação, rotina de 4 semanas).
- `google-ads/palavras-chave.csv` (37), `negativas.csv` (28), `anuncios.csv` (5 RSAs, 12 títulos + 4 descrições cada, limites de caracteres validados por script). Formato para o Google Ads Editor.

## 5. Pendências, em ordem de prioridade

| # | Pendência | Prioridade | Depende de | Próximo passo |
|---|---|---|---|---|
| 1 | **Bloqueio ético: uso do caso concreto na publicidade** (ver §6) | **URGENTE, antes de ativar** | Sua decisão | Escolher entre A, B ou C (§6) |
| 2 | **Tag do Google ausente nas 3 páginas**: as conversões hoje não são medidas | Alta | ID `AW-…` e rótulo da conversão | Criar a ação no Google Ads e me passar o ID: aplico os 2 trechos (CAMPANHA.md §6) |
| 3 | **URL final**: onde as páginas serão publicadas | Alta | Você / hospedagem | Os links internos são relativos (`dano-moral.html` etc.), o que indica a mesma pasta das demais páginas do site. Os links do Drive apontam para `junkesadvocacia.com.br/paginas/…`. **Confirmar** e publicar. |
| 4 | Orçamento diário e teto de CPC | Média | Você | Abrir o Planejador de palavras-chave com o CSV e definir. |
| 5 | Peso das páginas: 0,7 a 1,46 MB, por imagens embutidas em base64 | Média | — | Afeta o carregamento no celular e a "experiência na página de destino" do Ads. Melhoria possível: extrair as imagens para arquivos `.webp`. **Não fiz**, porque altera páginas aprovadas. |
| 6 | Sem `<link rel="canonical">` e sem dados estruturados (`LegalService`) | Baixa | URL final (#3) | Acrescentar depois da publicação. |

## 6. Bloqueio ético — o ponto que não pode ser escondido

**O fato:** a campanha é **publicidade paga** (impulsionamento) e leva a uma página cujo argumento central é um **caso concreto patrocinado pelo escritório**. A página traz o número do processo, a linha do tempo, "3 votos a 0", "decisão definitiva" e CTAs como "Quero saber se o meu caso é parecido". A linha "Fase de cumprimento de sentença — Em andamento" deixa claro que o escritório atua no caso.

**A norma:** pesquisa feita agora, em fontes secundárias, indica que o **Provimento 205/2021 do CFOAB veda, em qualquer publicidade, "o uso de casos concretos para oferta de atuação profissional"** e a promessa de resultados. Indica também que ementas dos Tribunais de Ética aplicam essa vedação inclusive a redes sociais (são citados os arts. 4º, §2º, 5º, §3º e 6º, sem confirmação da numeração). **Não consegui abrir o texto oficial** (oab.org.br bloqueado neste ambiente). **Confira a numeração e a redação no site do CFOAB antes de decidir.**

**Pontos a favor da página como está:**
- tom informativo, sem promessa, com seção de decisões contrárias;
- partes não identificadas e decisões públicas;
- rodapé que invoca o Provimento.

**Pontos contra, e mais fortes:**
- **O número do processo identifica as partes.** Qualquer pessoa consulta o PJe-TJPB e vê os nomes das clientes. A frase do rodapé "apresentadas sem identificação das partes" fica, na prática, inexata.
- O caso é usado **para oferecer atuação**: o CTA é literalmente "veja se o seu é parecido". É o núcleo da vedação.
- Com Google Ads, a página deixa de ser publicidade passiva e passa a ser **publicidade ativa**, mais exposta a representação, inclusive de concorrentes.
- Risco reputacional e disciplinar (censura) desproporcional ao ganho, porque a página sem o caso continua forte.

**Alternativas:**

| Opção | O que muda | Risco ético | Força comercial |
|---|---|---|---|
| **A. Manter como está** | Nada | **Alto** | Máxima |
| **B. Jurisprudência, não "nosso caso"** *(recomendada)* | Retirar o número do processo, a linha do tempo de datas, "cumprimento de sentença" e o vínculo com o escritório. Apresentar como "**o que o TJPB decidiu** sobre bloqueio de contas", com os 6 fundamentos e os trechos do acórdão (que são públicos e úteis). `caso-real.html` vira "entendimento do tribunal" ou sai do ar. | Baixo/moderado | Alta: os fundamentos são o que convence, não o placar |
| **C. Manter o caso só no orgânico** | Google Ads aponta para uma versão B; a versão atual fica sem impulsionamento | Moderado | Alta |

Também vale confirmar se as clientes **autorizaram por escrito** a divulgação, mesmo anonimizada. Isso não afasta a vedação do Provimento, mas reduz o risco quanto ao sigilo.

**Não fiz a versão B** porque ela reescreve conteúdo aprovado e a decisão é sua. Se escolher B ou C, preparo `defesa-vendedor-ads.html` como **arquivo novo**, sem tocar nos atuais.

## 7. Plano para continuar

1. **Você:** decidir A/B/C (§6) e conferir o texto oficial do Provimento 205/2021.
2. **Você:** criar a ação de conversão no Google Ads e me passar o `AW-…/rótulo`. **Eu:** instalar a tag nas páginas (CAMPANHA.md §6).
3. **Você:** confirmar a URL final e publicar.
4. **Você:** importar os CSVs no Google Ads Editor e definir o orçamento; **campanha pausada** até os itens 1–3.
5. Ativar e seguir a rotina de 4 semanas (CAMPANHA.md §8).
