# Página Amazon + Campanha Google Ads — Diagnóstico e estado (atualizado em 12/10/2026)

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

## 4-A. Refino para publicação (12/10/2026)

**Publicar os arquivos da pasta `publicar/`** (ou `publicar.zip`). Os originais aprovados continuam intactos em `site/`. O script `tools/refinar.py` refaz tudo a partir deles.

**Conteúdo:** o texto visível ficou idêntico, com uma única exceção (verificado por diff). No rodapé, "sem identificação das partes" virou "sem os nomes das partes", porque o número do processo permite consultar as partes no PJe.

**Citações conferidas com os autos (PDFs do Drive):**
- os 6 trechos do acórdão da página principal;
- os 7 trechos do acórdão e os 6 da sentença na página do caso;
- as 5 teses da ementa ("na íntegra");
- relator, unanimidade, REsp 1.978.268/SP e AREsp 2.911.102/SP, data de assinatura (01/09/2026), lucros cessantes negados e perda de uma chance absorvida no dano moral.

Tudo confere literalmente. Ficaram sem conferência só os trechos das notificações da Amazon e as datas da sessão virtual (24 a 31/08), que estão nos autos completos (PDF de 13 MB), não no acórdão nem na sentença.

| Ajuste | Por quê |
|---|---|
| Avaliações em movimento contínuo (a pedido, 12/10), sem cópias embutidas no arquivo; na página principal, duas fileiras em sentidos opostos | As cópias do laço passam a ser feitas pelo navegador: o arquivo continua leve e não aparece card repetido ou cortado parado. Quem ativou "reduzir movimento" no aparelho vê a faixa parada, com rolagem. |
| Imagens em WebP, com width/height | Peso: principal 1,42 MB → 0,64 MB; caso 0,78 → 0,37; contato 0,69 → 0,31. Carrega mais rápido no celular e melhora a nota de experiência da página no Google Ads. |
| Algarismos alinhados na fonte dos títulos | A Playfair usava algarismos antigos: "3 votos a 0" aparecia como "3 votos a o", e "01", "02" como "o1", "o2". |
| Margem lateral do banner final | O bloco "Fale no WhatsApp" encostava na borda da tela no celular e ficava desalinhado no computador. |
| Botões "Isso aconteceu comigo" com contorno, em vez de verde cheio | Seis botões verdes seguidos competiam com o botão principal. Os links e o texto foram mantidos. |
| Marca repetida no topo do hero oculta só no celular | A marca já está na barra fixa; a repetição empurrava o título para baixo. |
| Contato: foto oculta no celular | No celular, a foto ocupava a tela inteira antes do formulário. |
| Tag do Google Ads pronta, desligada | Basta preencher `window.JUNKES_ADS` (ver CAMPANHA.md §6). Conversão testada nos links e no formulário. |
| Dados estruturados `LegalService` e `theme-color` | SEO local. Avaliações **não** foram marcadas como `aggregateRating`, porque o Google não aceita avaliações publicadas pelo próprio negócio. |

Guia de execução da campanha, com blocos para copiar e colar: `google-ads/PASSO-A-PASSO.md`.

## 5. Pendências, em ordem de prioridade

| # | Pendência | Prioridade | Depende de | Próximo passo |
|---|---|---|---|---|
| 1 | ~~Uso do caso concreto na publicidade~~ (ver §6) | — | — | **Decidido em 12/10: opção A, manter o caso como está.** O risco foi apontado e assumido pelo titular. |
| 2 | **Conversão do Google Ads**: código pronto nas páginas, falta o ID | Alta | ID `AW-…` e rótulo da conversão | Criar a ação no Google Ads e preencher `window.JUNKES_ADS` nos 3 arquivos (CAMPANHA.md §6) |
| 3 | ~~URL final~~ | — | — | **Confirmada em 12/10: `https://junkesadvocacia.com.br/paginas/`.** Canonical, og:url, og:image e URL final dos anúncios já preenchidos. |
| 4 | Orçamento diário e teto de CPC | Média | Você | Abrir o Planejador de palavras-chave com o CSV e definir. |
| 5 | ~~Peso das páginas~~ | — | — | **Resolvido em 12/10**: as páginas caíram para menos da metade do peso (ver §4-A). |
| 6 | ~~Canonical e og:image~~ | — | — | **Resolvido em 12/10.** Subir também `og-defesa-vendedor.jpg` na mesma pasta. |

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

1. ~~Decidir A/B/C~~: **opção A escolhida em 12/10** (manter o caso).
2. **Você:** criar a ação de conversão no Google Ads e me passar o `AW-…/rótulo`. **Eu:** instalar a tag nas páginas (CAMPANHA.md §6).
3. **Você:** confirmar a URL final e publicar.
4. **Você:** importar os CSVs no Google Ads Editor e definir o orçamento; **campanha pausada** até os itens 1–3.
5. Ativar e seguir a rotina de 4 semanas (CAMPANHA.md §8).
