# Instruções para o Claude: corrigir a campanha no Google Ads

> **Como usar:** abra o Google Ads no Chrome, já logado na conta, e entregue este documento inteiro ao Claude com a extensão Claude no Chrome (ou outro Claude que opere o navegador). Ele executa as tarefas na ordem e devolve um relatório.

---

## Contexto

Você vai operar o painel do Google Ads do advogado **Hemerson Henrique Junkes (OAB/PR 85.858)**, que já está logado no navegador.

- **Conta:** 959-986-1021 (Junkes Advocacia), usuário junkes.adv@gmail.com
- **Campanha:** `[PESQUISA] [AMAZON-VENDEDOR] [BR]`, do tipo Pesquisa, com 4 grupos de anúncios:
  - `GC - Conta desativada`
  - `GS - Saldo retido`
  - `GA - Advogado e ação contra Amazon`
  - `GE - Amazon EUA`
- **Início programado:** 26/10/2026. A campanha **não pode começar antes disso**.
- **Página de destino:** `https://junkesadvocacia.com.br/paginas/defesa-vendedor.html`

A campanha já foi revisada. O que está certo **não deve ser alterado**:
- só Rede de Pesquisa (sem Display e sem Parceiros);
- Brasil, idioma Português;
- R$ 50/dia, lance "Maximizar cliques";
- AI Max, correspondência ampla e recursos automáticos desligados;
- as 48 palavras-chave negativas;
- a aplicação automática de recomendações desligada.

---

## Regras obrigatórias

1. **Não adicione fundos, não altere a forma de pagamento e não aceite termos financeiros.**
2. **Não remova nem exclua** campanhas, grupos, anúncios, palavras-chave ou negativas. Altere só o que está listado abaixo.
3. **Não mude** orçamento, estratégia de lance, data de início, locais, idioma nem redes, exceto onde a tarefa mandar.
4. **Não ative** sugestões do Google que aparecerem: AI Max, correspondência ampla, "aplicar recomendação", "otimizar" e similares. Feche os pop-ups com "Dispensar" ou "X".
5. **Nunca digite senhas nem códigos de verificação.** Se o Google pedir confirmação de identidade, pare e peça ao usuário.
6. Se a interface for diferente do descrito, ou se uma ação parecer irreversível, **pare e pergunte ao usuário** antes de continuar.
7. Se o Chrome estiver traduzindo a página (aparece "Google Anúncios", "Almirante", "Disfarce"), desligue a tradução para este site antes de começar.
8. Clique em **Salvar** ao final de cada alteração e confira se ela foi aplicada.

---

## Tarefas (nesta ordem)

### Tarefa 1: reativar o grupo "GC - Conta desativada"
O grupo está pausado por engano. É o grupo principal da campanha.
1. **Campanhas → Grupos de anúncios**, filtrando pela campanha `[PESQUISA] [AMAZON-VENDEDOR] [BR]`.
2. Na linha `GC - Conta desativada`, clique na bolinha de status e escolha **Ativar**.
3. **Conferir:** o status do grupo fica "Ativado". Pode continuar aparecendo "Não qualificada – a campanha está pendente"; isso é normal até 26/10.

### Tarefa 2: programação de anúncios para todos os dias, das 07h às 23h
Hoje está de segunda a sexta, das 06:00 às 00:00, sem fim de semana.
1. Dentro da campanha: **Públicos-alvo, palavras-chave e conteúdo → Programação de anúncios** → lápis (editar).
2. Deixe **7 linhas**, uma por dia, de segunda a domingo, das **07:00 às 23:00**. Uma alternativa é a opção "Todos os dias" com 07:00–23:00.
3. Remova as linhas antigas de 06:00–00:00.
4. **Salvar.**
5. **Conferir:** a tabela mostra os 7 dias, de 07:00 a 23:00.

### Tarefa 3: limite de lance de CPC
1. **Configurações da campanha → Lances** (expandir).
2. A estratégia deve continuar **Maximizar cliques**. Marque **"Definir um limite máximo de lance de CPC"** = **R$ 8,00**.
3. **Salvar.**
4. **Conferir:** "Lances" mostra Maximizar cliques com limite de R$ 8,00.

### Tarefa 4: opção de local
1. **Configurações da campanha → Locais** (expandir) → **Opções de local**.
2. Em "Incluir", marque **"Presença: pessoas que estão ou costumam estar nos locais incluídos"**. Não use a opção de "interesse".
3. **Salvar.**

### Tarefa 5: recursos (sitelinks, frases de destaque, ligação)
Adicione no **nível da campanha**, por **Recursos → +**, ou pela seção de recursos dentro da campanha.

**5a. Sitelinks** (4). Use as descrições só se o formulário exigir.

| Texto do sitelink | URL final | Descrição 1 | Descrição 2 |
|---|---|---|---|
| O caso completo | `https://junkesadvocacia.com.br/paginas/caso-real.html` | Do bloqueio à decisão final | Decisão do TJPB, explicada |
| Fale com o escritório | `https://junkesadvocacia.com.br/paginas/contato-vendedor.html` | Conte seu caso pelo WhatsApp | Atendimento online no Brasil |
| O que separar | `https://junkesadvocacia.com.br/paginas/defesa-vendedor.html#documentos` | Prints, e-mails e relatórios | Lista para agilizar a análise |
| Fundamentos | `https://junkesadvocacia.com.br/paginas/defesa-vendedor.html#fundamentos` | O que o tribunal considerou | Em linguagem simples |

**5b. Frases de destaque** (4):
- Atendimento online
- Processo eletrônico
- Análise sem promessas
- Sigilo profissional

**5c. Ligação:** país **Brasil**, número **(41) 99599-2256**. Ative o relatório de chamadas se o formulário oferecer.

**Conferir:** em Recursos aparecem 4 sitelinks, 4 frases de destaque e 1 ligação, todos com nível "Campanha".

### Tarefa 6: URL final de todos os anúncios
1. **Campanhas → Anúncios**, filtrando pela campanha. Devem existir 4 anúncios, um por grupo.
2. Abra uma nova aba e acesse `https://junkesadvocacia.com.br/paginas/defesa-vendedor.html`.
   - **Se a página abrir:** continue.
   - **Se der erro (404, página inexistente):** não altere nada nesta tarefa. Anote "página ainda não publicada" no relatório e siga para a Tarefa 7.
3. Para cada anúncio, confira a **URL final** (não o "caminho de exibição"). Se for diferente de `https://junkesadvocacia.com.br/paginas/defesa-vendedor.html`, edite, troque e salve. O caminho de exibição (ex.: `advogado/saldo-retido`) pode ficar como está.
4. **Não altere** títulos nem descrições.
5. **Conferir:** anote no relatório, para cada anúncio, o grupo, a URL final e o status (ex.: "Em análise", "Aprovado", "Reprovado" com o motivo).

### Tarefa 7: anúncios políticos na União Europeia
1. **Adm. → Política → Conta** (Verificação do anunciante).
2. Abra a tarefa **"Confirmar se você veicula anúncios políticos na UE"**. Se já estiver concluída, use "Editar".
3. Responda **NÃO**: o anunciante **não** veicula anúncios políticos na UE. Salve.
4. **Conferir:** o texto passa a dizer que você **não** veicula anúncios políticos na UE.

### Tarefa 8: criar a conversão "Clique no WhatsApp"
1. **Metas → Conversões → Resumo → + Criar ação de conversão → Site**.
2. Domínio: `junkesadvocacia.com.br` → **Verificar** → **Adicionar uma ação de conversão manualmente**.
3. Preencha:
   - Meta e ação: categoria **Contato**
   - Nome da ação: **Clique no WhatsApp**
   - Valor: **Não usar um valor**
   - Contagem: **Uma**
   - Mantenha o restante no padrão.
4. **Concluído / Salvar e continuar** → na configuração da tag, escolha **"Instalar a tag você mesmo"** → aba **"Snippet de evento"** (ou "Usar o Gerenciador de tags do Google: não").
5. **Copie o trecho completo do snippet de evento.** Ele contém `send_to: 'AW-XXXXXXXXX/XXXXXXXXXXX'`. Coloque o snippet **inteiro** no relatório.
6. **Não** tente instalar a tag no site. Isso será feito por outra pessoa.

### Tarefa 9: meta de conversão da campanha
Faça **só depois** de concluir a Tarefa 8.
1. **Configurações da campanha → Metas de conversão** → **"Usar metas de conversão específicas da campanha"**.
2. Selecione **apenas** a meta **Contato**. Dentro dela, se o painel permitir escolher ações, deixe só **Clique no WhatsApp**. Desmarque "Lead telefônico" e as demais.
3. **Salvar.**
4. A estratégia de lance deve **continuar** "Maximizar cliques". Se o Google sugerir mudar, recuse.

### Tarefa 10: conferência final (sem alterar nada)
Abra **Configurações da campanha** e confirme cada item:

| Item | Valor esperado |
|---|---|
| Status da campanha | Ativado (status de veiculação "Pendente" até 26/10) |
| Redes | Só Rede de Pesquisa do Google |
| Orçamento | R$ 50,00/dia |
| Lances | Maximizar cliques, limite de CPC R$ 8,00 |
| Locais | Brasil, opção "Presença" |
| Idioma | Português |
| Data de início | 26/10/2026, sem término |
| AI Max / correspondência ampla / recursos automáticos | Desligados |
| Programação | Todos os dias, 07:00–23:00 |
| Grupos de anúncios | Os 4 com status Ativado |
| Faturamento | Saldo R$ 0,00. **Não alterar.** |

---

## Relatório para devolver ao usuário

Ao terminar, responda neste formato:

```
RELATÓRIO – Google Ads – [data e hora]

Tarefa 1 (grupo GC): [feito / não feito – motivo]
Tarefa 2 (programação 7 dias 07–23h): [...]
Tarefa 3 (limite CPC R$ 8): [...]
Tarefa 4 (opção de local presença): [...]
Tarefa 5 (sitelinks / frases / ligação): [...]
Tarefa 6 (URL final dos 4 anúncios):
  - GC: URL ___ | status ___
  - GS: URL ___ | status ___
  - GA: URL ___ | status ___
  - GE: URL ___ | status ___
  Página de destino abriu? [sim / não]
Tarefa 7 (UE = Não): [...]
Tarefa 8 (conversão): [feito] – SNIPPET COMPLETO:
  [colar aqui]
Tarefa 9 (meta da campanha): [...]
Tarefa 10 (conferência): [itens divergentes, se houver]

Pendências ou dúvidas para o usuário: [...]
```

O usuário vai repassar esse relatório, principalmente o **snippet da Tarefa 8**, para concluir a instalação da medição nas páginas do site.
