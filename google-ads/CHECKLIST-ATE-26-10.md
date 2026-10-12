# Roteiro: campanha pronta para começar sozinha em 26/10/2026

Conta Google Ads 959-986-1021 (junkes.adv@gmail.com). Situação em 12/10/2026, pelo print do painel:

- conta **cancelada** (sem anúncios há muito tempo);
- pagamento **pré-pago via Pix**, saldo **R$ 0,00**;
- campanha antiga **"Advogados de Qualidade" marcada como ativa**;
- 14 ações de conversão antigas (1 com tag inativa, 13 sem conversões recentes).

O Google Ads não está conectado a esta sessão: os passos são feitos por você no painel. Os textos para colar estão em `PASSO-A-PASSO.md`.

---

## Pente fino da conta (PDF de 12/10/2026, 11:16–11:39)

| Item | Situação | Ação |
|---|---|---|
| Status da conta | **Ativa** (reativada às 11:37) | — |
| 12 campanhas antigas | Todas **Removidas** | Nenhuma. "Removida" é o estado final do Google Ads; não existe exclusão além disso. |
| Recursos antigos (sitelinks, chamadas etc.) | Nenhum ativo | — |
| Verificação do anunciante | Concluída (2023 e 2025); anúncios aparecem como "pagos por HEMERSON HENRIQUE JUNKES" | — |
| Usuários | Só junkes.adv@gmail.com, com verificação em duas etapas | Opcional: criar a chave de acesso (Adm → Acesso e segurança) |
| **Aplicação automática de recomendações** | **8 tipos ligados** (incl. trocar estratégia de lance, "remover negativas em conflito", segmentação otimizada) | **Desligar todos** (passo 0 abaixo) |
| Pendência de política: anúncios políticos na UE | Aberta | Responder **Não** |
| Pendência: quem paga os anúncios | Opcional | Pode ignorar (já mostra o seu nome) |
| Conversões antigas (14, incl. "[Clicou] [Botão WhatsApp]") | Sem uso | Não mexer. A campanha nova usará só a conversão nova, como meta específica da campanha. |
| Saldo | R$ 0,00 · recarga automática desativada | Adicionar em 23–24/10 |

### 0. Desligar a aplicação automática (obrigatório)
- [ ] **Recomendações → Configurações de aplicação automática → Gerenciar**.
- [ ] Nos dois quadros ("Mantenha seus anúncios" e "Amplie seus negócios"), **desmarcar todas as caixas** e salvar.
- [ ] Conferir em **Adm. → Configurações da conta → Aplicação automática**: deve aparecer "Nenhuma" (ou equivalente).

Por quê: ligada, ela troca o lance de "Maximizar cliques" para "Maximizar conversões/CPA desejado", pode **remover as palavras negativas** e ampliar a segmentação, sem aviso e gastando o orçamento.

### 0b. Anúncios políticos na UE
- [ ] **Adm. → Política → Conta → Confirm if you plan to run EU political ads → Start task → "Não"**.

## Fase 1 — Agora, antes da viagem (≈ 40 min)

### 1. Reativar a conta
- [x] **Feito em 12/10** (conta ativa às 11:37; verificação do anunciante já estava concluída).

### 2. Pausar a campanha antiga (antes de pôr qualquer saldo)
- [x] **Feito em 12/10**: as 12 campanhas antigas estão "Removidas".

### 3. Criar a conversão nova
- [ ] **Metas → Conversões → Resumo → + Nova ação de conversão → Site**.
- [ ] Domínio: `junkesadvocacia.com.br` → **Adicionar uma ação de conversão manualmente**.
- [ ] Categoria **Contato** · Nome **Clique no WhatsApp** · Valor: **não usar** · Contagem: **Uma**.
- [ ] **Concluir** → configurar a tag → **Instalar a tag você mesmo** → **Snippet de evento**.
- [ ] Copie o trecho que contém `send_to: 'AW-.........../..........'` e **envie para o Claude** (texto ou print).

### 4. Criar a campanha (fica agendada, não pausada)
**Campanhas → + Nova campanha → Criar uma campanha sem orientação de meta → Pesquisa**.

| Campo | Valor |
|---|---|
| Nome | `Defesa do Vendedor - Pesquisa` |
| Redes | desmarcar **Parceiros de pesquisa** e **Rede de Display** |
| Locais | **Brasil** · Opções: **Presença: pessoas que estão ou costumam estar** |
| Idiomas | **Português** |
| **Mais configurações → Data de início** | **26/10/2026** · Data de término: **nenhuma** |
| **Programação de anúncios** | **Todos os dias, 07:00 às 23:00** |
| Metas | **Usar metas específicas da campanha** → só **Clique no WhatsApp** |
| Lances | **Maximizar cliques** · marcar **limite máximo de lance de CPC: R$ 8,00** |
| Orçamento | **R$ 50,00 por dia** |
| Grupos de anúncios | os 5 grupos do `PASSO-A-PASSO.md` (palavras-chave + anúncio) |
| URL final | `https://junkesadvocacia.com.br/paginas/defesa-vendedor.html` |
| Recursos | sitelinks, frases de destaque e ligação do `PASSO-A-PASSO.md` |

- [ ] Depois de criar: **Palavras-chave → Negativas** → colar a lista do `PASSO-A-PASSO.md`.
- [ ] Status esperado: **"Qualificada (programada)"** ou **"Ainda não começou"**. É assim mesmo: ela começa sozinha em 26/10.

Com saldo R$ 0,00 nada é gasto, mesmo que algo esteja ativo por engano.

---

## Fase 2 — Quando o Claude devolver as páginas com a conversão
- [ ] Subir os 3 arquivos novos em `/paginas/`, substituindo os atuais.
- [ ] Abrir `junkesadvocacia.com.br/paginas/defesa-vendedor.html`, clicar no WhatsApp.
- [ ] Em até 24 h, **Metas → Conversões**: "Clique no WhatsApp" deve sair de "Não verificado" para **"Gravando conversões"** ou "Nenhuma conversão recente" (tag ativa).

---

## Fase 3 — 23 ou 24/10, antes de voltar
- [ ] **Faturamento → Adicionar fundos → Pix: R$ 1.500** (≈ 30 dias × R$ 50). Pode pôr R$ 750 e completar depois.
- [ ] Conferir de novo: campanha antiga **pausada**; campanha nova com início **26/10**.
- [ ] WhatsApp Business: mensagem de **ausência** e **saudação** configuradas.

## Fase 4 — 26/10 em diante
- [ ] Dia 26: os anúncios começam sozinhos às 7h. Confira à tarde se há **impressões**.
- [ ] A cada 2–3 dias na 1ª semana: **Palavras-chave → Termos de pesquisa** → negativar o que não for de vendedor.
- [ ] Sem mexer no orçamento por 4 semanas. Na 4ª semana, revisar com o Claude.
