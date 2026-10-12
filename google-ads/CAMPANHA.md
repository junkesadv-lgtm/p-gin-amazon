# Campanha Google Ads — Defesa do Vendedor (Amazon)

Rede de Pesquisa. Página de destino: `https://junkesadvocacia.com.br/paginas/defesa-vendedor.html` (já preenchida em `anuncios.csv`), com `caso-real.html` e `contato-vendedor.html` como apoio.

> **Antes de ativar:** leia o item "Bloqueio ético" em `../STATUS.md`. A campanha está pronta para ser montada, mas não deve ser ativada antes dessa decisão.

## 1. Configuração da campanha

| Item | Configuração | Por quê |
|---|---|---|
| Tipo | Pesquisa (somente) | Quem procura "conta de vendedor desativada" já tem o problema. Display e Performance Max dispersam verba nesta fase. |
| Redes | Desmarcar **Parceiros de pesquisa** e **Rede de Display** | Tráfego mais barato, mas de qualidade difícil de controlar. |
| Local | Brasil, opção **"Presença: pessoas que estão ou costumam estar"** | Evita cliques de quem só tem interesse no Brasil. |
| Idioma | Português | — |
| Lances (semanas 1–3) | **Maximizar cliques** com teto de CPC, ou CPC manual | Sem histórico de conversões, o lance automático por conversão não tem dados. |
| Lances (depois) | **Maximizar conversões** quando houver ~15–30 conversões em 30 dias | Limiar prático; confirmar no painel. |
| Programação | Horário em que o WhatsApp é respondido | Lead que espera horas para ter resposta esfria. |
| Orçamento diário | **A definir por você** | Não estimei CPC: os valores reais aparecem no Planejador de palavras-chave da sua conta, que não consigo acessar daqui. |

## 2. Grupos de anúncios

Arquivo `palavras-chave.csv` (37 termos, correspondência de frase + exata nos termos mais fortes).

| Grupo | Intenção | Exemplos |
|---|---|---|
| 01 Conta desativada | Problema, sem saber a solução | conta de vendedor amazon desativada; seller central suspenso |
| 02 Saldo retido | Problema financeiro (dano material mais claro) | saldo retido amazon; amazon não libera meu dinheiro |
| 03 Advogado | **Maior intenção de contratar** | advogado para vendedor amazon; processo contra amazon vendedor |
| 04 Acusações | Fraude, inautenticidade, conta vinculada, dropshipping | amazon acusou vendedor de fraude; conta vinculada amazon suspensa |
| 05 Amazon EUA | Vendedor no Brasil com conta na Amazon.com | conta amazon.com bloqueada |

Os termos vieram da lista de 50 páginas SEO do "Relatório de geração de páginas SEO — Amazon Seller" (Drive, pasta 06).

**Prioridade de verba:** 03 > 02 > 01 > 04 > 05. O grupo 05 tem volume provavelmente baixo e tese menos pacífica, já que a própria página reconhece divergência entre tribunais.

## 3. Palavras negativas

Arquivo `negativas.csv` (28 termos). Eles excluem quem procura emprego, cursos, modelos, login e SAC, além de **compradores** com problema de entrega, que são outro público. Na primeira semana, revise o **Relatório de termos de pesquisa** a cada 2–3 dias e acrescente negativas.

## 4. Anúncios responsivos (RSA)

Arquivo `anuncios.csv`: 1 RSA por grupo, 12 títulos (máx. 30 caracteres) e 4 descrições (máx. 90). Os limites foram conferidos por script.

Critérios do texto:
- **Nenhum anúncio menciona o caso julgado, vitória, "3 votos a 0" ou resultado.** Anúncio pago é publicidade ativa, e é nele que o risco ético é maior (ver STATUS.md).
- Nada de promessa ("recupere seu saldo", "reative sua conta"). Os textos falam em "análise técnica", "sem promessas" e "se não houver caminho, você saberá", alinhados com a própria página.
- **A palavra "Amazon" só aparece no grupo 05 ("Amazon.com").** Nos demais grupos o termo da marca fica na palavra-chave, não no texto. O motivo é que a política de marcas registradas do Google pode reprovar anúncios com o nome de terceiros se o titular tiver registrado restrição. Se quiser testar "Amazon" nos títulos, faça isso em um anúncio separado, para não derrubar o principal.

## 5. Recursos (extensões)

- **Sitelinks:** "O caso completo" → `https://junkesadvocacia.com.br/paginas/caso-real.html`; "Fale com o escritório" → `https://junkesadvocacia.com.br/paginas/contato-vendedor.html`; "O que separar" → `https://junkesadvocacia.com.br/paginas/defesa-vendedor.html#documentos`; "Fundamentos" → `https://junkesadvocacia.com.br/paginas/defesa-vendedor.html#fundamentos`.
- **Frases de destaque:** Atendimento online · Processo eletrônico · Análise sem promessas · Sigilo profissional.
- **Ligação / WhatsApp:** (41) 99599-2256.
- **Snippet estruturado — Serviços:** Conta desativada; Saldo retido; Conta vinculada; Inautenticidade.

## 6. Medição de conversões — **pendente, bloqueia a otimização**

As páginas **já disparam** o evento `whatsapp_click` (com `cta` e `page`) via `gtag` e `dataLayer` em todo link `data-cta` e no envio do formulário. **Porém nenhuma das três páginas tem a tag do Google instalada**, então hoje esses eventos não chegam a lugar nenhum.

**Atualização (12/10):** as páginas da pasta `publicar/` já trazem o carregamento da tag e o disparo da conversão. Basta:

1. No Google Ads: *Metas → Conversões → Nova ação → Site* → criar **"Clique no WhatsApp"** (categoria *Contato*, contagem **Uma**) e anotar o ID `AW-XXXXXXXXX` e o rótulo.
2. Em cada um dos 3 arquivos de `publicar/`, preencher a linha (fica no `<head>`):
   `window.JUNKES_ADS = { id: 'AW-XXXXXXXXX', label: 'ROTULO' };`
3. Testar com o **Tag Assistant** antes de ativar a campanha.

Com os campos em branco, nada é carregado. A conversão dispara em todo botão de WhatsApp e no envio do formulário (testado com ID fictício).

**Limitação a conhecer:** clique no WhatsApp ≠ cliente. Para saber o custo real por contrato, anote na planilha de atendimento de onde veio cada contato ("Vim pelo site…": as mensagens pré-preenchidas já identificam a página e o botão).

## 7. Como importar

Google Ads Editor → *Conta → Importar → De arquivo* → importar `palavras-chave.csv`, `negativas.csv` e `anuncios.csv`. Antes, crie a campanha "Defesa do Vendedor - Pesquisa". A URL final já vem no `anuncios.csv`.

## 8. Rotina das 4 primeiras semanas

| Quando | O quê |
|---|---|
| Dias 1–3 | Conferir se as conversões estão registrando; termos de pesquisa → negativas |
| Semana 1 | Pausar palavras com gasto e zero clique no WhatsApp; ver se os anúncios foram aprovados |
| Semana 2 | Comparar grupos por custo/clique no WhatsApp; deslocar verba para o melhor |
| Semana 3–4 | Com conversões suficientes, mudar para *Maximizar conversões* |
