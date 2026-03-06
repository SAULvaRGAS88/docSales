# DwuSales

Este documento descreve, de forma resumida e clara, o que o aplicativo faz: as telas, os fluxos e as funcionalidades disponíveis ao usuário. A ordem das seções segue o menu principal do aplicativo.

---

## 1. Acesso e configuração inicial

### 1.1 Tela de configuração da empresa (antes do login)

- O usuário informa o **código da empresa** (cliente) e clica em **Buscar Empresas**.
- O sistema busca e exibe as **bases de dados** disponíveis para aquela empresa.
- O usuário escolhe qual base utilizar e clica em **Salvar**.
- Os dados da empresa são gravados no aparelho. Em seguida, o usuário é direcionado para a tela de login.

<img width="446" height="935" alt="image" src="https://github.com/user-attachments/assets/e43c7430-364b-4ecf-abd5-2db72bcbac29" /> 

### 1.2 Tela de login

- O usuário informa **usuário** e **senha** e pode marcar a opção de **salvar a senha** para uso offline.
- Na primeira vez, o aplicativo pode pedir a **escolha do idioma** (ex.: português, inglês, espanhol).
- Há um link para **Configuração**, que leva de volta à tela onde se informa o código da empresa e a base de dados.
- O login é validado na internet. Quando válido, o aplicativo pode iniciar uma **sincronização inicial** dos dados (carga inicial) e, ao final, levar o usuário ao **Dashboard**.

<img width="446" height="935" alt="image" src="https://github.com/user-attachments/assets/4c79def6-42b8-4d1a-b0ea-520bd3675dd0" />
<img width="446" height="935" alt="image" src="https://github.com/user-attachments/assets/d4eab100-3113-461c-ab14-e1ce54e3cdf7" /> <img width="446" height="935" alt="image" src="https://github.com/user-attachments/assets/7f9ac4f7-0a1a-4a94-9993-2fe2e74ee4ad" />

---

## 2. Painel principal (Dashboard)

- O **Dashboard** é a tela inicial após o login.
- Mostra um **resumo** do que é importante para o dia a dia: indicadores de atendimentos (em atraso, para hoje, futuros), cotações em aberto, pedidos em aberto, leads, clientes, clientes sem compras, documentos pendentes, rascunhos e falhas de envio.
- O usuário pode ver a **meta do mês atual** (vendas) e um **gráfico** de desempenho.
- Há um **botão de sincronização** para atualizar os dados manualmente.
- É possível abrir avisos sobre **tabelas com problema** na sincronização e sobre **documentos pendentes ou rascunhos**.
- Em empresas com mais de uma filial, o aplicativo pode pedir que o usuário escolha **filial** e **utilização** na primeira vez (configuração inicial).
- O usuário pode acessar o **menu lateral** (ícone de menu) para ir a qualquer outra tela do aplicativo.

  <img width="446" height="935" alt="image" src="https://github.com/user-attachments/assets/22651b45-1bce-4c96-8833-fcd106acb2e7" />  <img width="446" height="935" alt="image" src="https://github.com/user-attachments/assets/c32d9c3a-c8c9-4365-a79a-172ec189ad22" />
  <img width="446" height="935" alt="image" src="https://github.com/user-attachments/assets/9fc225c6-39ca-406a-afc5-8e8c03a7b0dc" />

---

## 3. Clientes

### 3.1 Lista de clientes

- Exibe a **lista de clientes** (parceiros de negócio) com busca por nome ou código.
- O usuário pode ver dados do cliente, **contatos** (telefone, e-mail) e **acessar no mapa**.
- É possível **ligar** ou **abrir WhatsApp** direto pelo aplicativo a partir dos contatos.

  <img width="446" height="935" alt="image" src="https://github.com/user-attachments/assets/a39e23a6-d420-43f8-a1af-467c44466fe2" />

### 3.2 Cadastro de parceiro de negócio (Cadastro PN)

- Permite **cadastrar** ou **editar** um cliente (parceiro de negócio).
- Inclui dados gerais, endereços de cobrança e entrega, contatos e características conforme a regra do negócio.
- O cadastro pode ser salvo **no aparelho** e enviado para o servidor quando houver conexão; é possível registrar a **localização (GPS)** no momento do cadastro.

  <img width="446" height="935" alt="image" src="https://github.com/user-attachments/assets/a62fd581-1ee1-4b45-a047-b17620f43684" /><img width="446" height="935" alt="image" src="https://github.com/user-attachments/assets/df7ec04c-b060-4037-9dd6-0dd7cf41c28f" />

---

## 4. Venda rápida

- É o módulo central para **fazer vendas no celular**.
- O usuário escolhe ou busca um **cliente**, monta um **carrinho** com itens, preços e quantidades.
- Permite criar **cotações** e **pedidos**, com opção de **rascunho** para continuar depois.
- O usuário pode ver **documentos** (cotações e pedidos) em aberto, pendentes ou com falha de envio, e **revisar ou reenviar** quando necessário.
- Há suporte a **múltiplos idiomas** e a uso **offline**: dados são gravados no aparelho e enviados quando a conexão estiver disponível.

  <img width="446" height="935" alt="image" src="https://github.com/user-attachments/assets/336d386b-808c-4980-a574-e3a5d38035bc" /><img width="446" height="935" alt="image" src="https://github.com/user-attachments/assets/64e1b017-ac95-4f60-bac9-02ad46a847a3" />
  <img width="446" height="935" alt="image" src="https://github.com/user-attachments/assets/10684ec4-8dab-43c6-8eab-de6496615a20" /><img width="446" height="935" alt="image" src="https://github.com/user-attachments/assets/92427866-f050-47c9-a621-7bfc5bb481fe" />
  <img width="446" height="935" alt="image" src="https://github.com/user-attachments/assets/f7394264-f241-4b77-9a34-b0d442bb5e28" /><img width="446" height="935" alt="image" src="https://github.com/user-attachments/assets/d3f878aa-5a97-421d-be63-2714a0d98063" />
  <img width="446" height="935" alt="image" src="https://github.com/user-attachments/assets/d516baaf-3b1c-4046-ab64-86f89811de93" /><img width="446" height="935" alt="image" src="https://github.com/user-attachments/assets/f3b3ee3f-7b36-4332-8bc7-582c04948654" />
  <img width="446" height="935" alt="image" src="https://github.com/user-attachments/assets/cad38261-08e6-4a6a-90c8-d46bd8aae3e7" /><img width="446" height="935" alt="image" src="https://github.com/user-attachments/assets/667b45f9-b127-4fcb-995b-89a0deb98e68" />

---

## 5. Vendas (Cotações e Pedidos)

### 5.1 Lista de cotações

- Lista as **cotações** do vendedor.
- O usuário pode **filtrar**, **ordenar** e **abrir** cada cotação para ver detalhes ou dar continuidade (por exemplo, converter em pedido), enviar espelho para seu cliente via compartilhamento ou direto pelo whatsapp.
- Um botão de ação rápida permite ir direto para **Venda Rápida** (nova cotação).

  <img width="446" height="935" alt="image" src="https://github.com/user-attachments/assets/ba95945b-f830-4245-bcdb-b38b37348bd4" /> <img width="491" height="578" alt="image" src="https://github.com/user-attachments/assets/70992647-dee3-4181-8536-555ef8e7e0f1" />

### 5.2 Lista de pedidos

- Lista os **pedidos** do vendedor.
- O usuário pode **filtrar**, **ordenar** e **abrir** cada pedido para ver detalhes.
- Um botão de ação rápida permite ir direto para **Venda Rápida** (novo pedido).

<img width="451" height="949" alt="image" src="https://github.com/user-attachments/assets/919a6075-0f31-45b1-a096-7db9b74b0241" />

---

## 6. Atendimento

### 6.1 Atendimentos

- Exibe a **lista de atendimentos** (visitas, contatos com clientes).
- O usuário pode **pesquisar**, **filtrar** e **ordenar**.
- Permite **criar novo atendimento** ver historico de pareceres, adicionar anexos e acessar a **Agenda** por um botão de ação rápida.

  <img width="451" height="949" alt="image" src="https://github.com/user-attachments/assets/a3e1b377-3732-4ba3-b6e5-f221fa743176" /> <img width="451" height="949" alt="image" src="https://github.com/user-attachments/assets/37a3e484-974b-4009-abfb-bbaa936feff2" />
  <img width="451" height="949" alt="image" src="https://github.com/user-attachments/assets/4e871825-0787-4224-b26b-ad630f049850" /><img width="451" height="949" alt="image" src="https://github.com/user-attachments/assets/121df42e-01a0-48b5-847f-586089f42c8e" />
  
### 6.2 Agenda

- Mostra um **calendário** com os atendimentos por data.
- O usuário vê atendimentos **para o dia**, **atrasados** e **futuros**.
- Ao tocar em um dia, são exibidos os atendimentos daquela data para consulta ou planejamento.

  <img width="451" height="949" alt="image" src="https://github.com/user-attachments/assets/3109c1df-f5cf-424b-941a-ea7e0d98d1c0" />

---

## 7. Relatórios

### 7.1 Relatórios de vendas faturadas

- Apresenta **relatórios de vendas** (faturadas), com visão por vendedor e por período.
- Inclui indicadores como **top clientes do mês**, **clientes sem compras**, **leads sem compras** e **clientes positivados**.
- O usuário pode **expandir** seções e ver detalhes dos itens faturados por pedido.

  <img width="451" height="949" alt="image" src="https://github.com/user-attachments/assets/a6f3d049-9b58-4166-a023-d47eb7c0d9f4" /><img width="451" height="949" alt="image" src="https://github.com/user-attachments/assets/fcba64b0-1fb7-4528-857e-bbe6d9c5b022" />


### 7.2 Metas do vendedor

- Exibe as **metas de vendas** do vendedor logado.
- Mostra o **desempenho por mês** (valor realizado x meta), em geral em forma de gráfico ou cards.
- Ajuda o vendedor a acompanhar se está no caminho da meta.

  <img width="451" height="949" alt="image" src="https://github.com/user-attachments/assets/39fe0cb6-d4b8-4ed1-b871-bbad1e71613c" /> <img width="451" height="949" alt="image" src="https://github.com/user-attachments/assets/8a547ab7-8f6a-40ec-854a-7a08ef025750" />

---

## 8. Mapa

- Exibe um **mapa** com a **localização do usuário** e dos **clientes** que possuem endereço com coordenadas.
- O usuário pode **buscar um cliente** e ver onde ele está no mapa.
- É possível **traçar rota** até o cliente e **abrir no Waze ou no Google Maps** para navegação.
- Clientes sem coordenadas podem ser listados em uma mensagem para que o usuário saiba que não aparecem no mapa.

  <img width="451" height="949" alt="image" src="https://github.com/user-attachments/assets/14a035a1-4225-451e-8864-04a14bc84c29" /><img width="451" height="949" alt="image" src="https://github.com/user-attachments/assets/4fe2ddec-2683-45e6-af98-2f04b9ab321a" />
  <img width="451" height="949" alt="image" src="https://github.com/user-attachments/assets/e87f09d3-8dfc-40a4-88ee-5d77b0ead668" /><img width="451" height="949" alt="image" src="https://github.com/user-attachments/assets/b6cb326e-4cf3-4125-8f79-a4697f1830c9" />

---

## 9. Sincronização

- Permite **escolher o que sincronizar**: clientes, itens e preços, estoque, atendimentos, cotações, pedidos, oportunidades, relatórios, configurações ou dados mestres.
- Há a opção de **sincronizar todos** os pacotes de uma vez.
- Ao confirmar, o aplicativo inicia a **carga/sincronização** (em outra tela de progresso), baixando e gravando no aparelho apenas o que foi selecionado.
- Útil para **atualizar dados** após um tempo sem uso ou quando algo foi alterado no sistema de origem.

<img width="451" height="949" alt="image" src="https://github.com/user-attachments/assets/6c6ae6cd-8fb9-49ef-ae21-2d42a3669387" />

---

## 10. Configuração (dentro do app)

- Mostra a **base de dados (empresa)** em uso e a **última vez que os dados foram sincronizados**.
- O usuário pode **trocar a filial** e a **utilização** padrão (quando a empresa tiver mais de uma).
- Permite **ajustar permissões** do aparelho (localização, câmera, armazenamento, notificações) e **abrir as configurações do sistema** se necessário.
- Inclui opções como **idioma do aplicativo**, **sincronização automática de cotações** (se existir) e outras preferências disponíveis na tela.
- Exibe a **versão do aplicativo**.

<img width="451" height="949" alt="image" src="https://github.com/user-attachments/assets/254b8607-8666-45fc-8464-6b57b9e7af70" />

---

## 11. Menu lateral e saída

- O **menu lateral** (ícone de barras no topo) lista todas as áreas do aplicativo na ordem descrita acima: Dashboard, Clientes (Lista e Cadastro PN), Venda Rápida, Vendas (Cotações e Pedidos), Atendimento (Atendimentos e Agenda), Relatórios (Vendas Faturadas e Metas Vendedor), Mapa, Sincronização e Configuração.
- O que aparece no menu pode **variar conforme as permissões** do usuário (por exemplo, só vê Cotações ou Pedidos se tiver permissão).
- No final do menu há a opção **Sair do aplicativo**, que encerra a sessão e, no Android, pode fechar o app (com confirmação).

<img width="451" height="949" alt="image" src="https://github.com/user-attachments/assets/633d5be0-a971-42f3-873f-d08f603dc8d7" />

---

## Resumo

O aplicativo permite que o vendedor:

- **Configure** a empresa e faça **login** com usuário e senha.
- Use um **painel (Dashboard)** com indicadores do dia a dia e meta do mês.
- **Consulte e cadastre clientes**, com lista, busca, contatos e mapa.
- **Faça vendas pelo celular** (Venda Rápida): cotações e pedidos, com suporte a rascunho e uso offline.
- **Acesse listas** de cotações e pedidos para filtrar, ordenar e abrir detalhes.
- **Gerencie atendimentos** e visualize a **agenda** no calendário.
- **Veja relatórios** de vendas faturadas e **acompanhe suas metas**.
- **Use o mapa** para localizar clientes e abrir rotas no Waze ou Google Maps.
- **Sincronize** os dados escolhendo o que atualizar (ou tudo).
- **Ajuste** filial, utilização, idioma e preferências na tela de Configuração.

Tudo em um único aplicativo, com foco em uso no campo, com ou sem internet, e em linguagem simples para o dia a dia do vendedor.
