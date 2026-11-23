# Mercado Regional


> Slogan: Gestão simples para fortalecer resultados:.

---

# 🎨 Paleta Oficial

| Cor | Código | Uso |
|-------|----------|----------|
| Verde Principal | `#42B883` | Botões e ações principais |
| Verde Petróleo | `#347474` | Menus e destaques |
| Azul Escuro | `#35495E` | Títulos e textos |
| Laranja | `#FF7E67` | Alertas e notificações |
| Branco | `#FFFFFF` | Fundo principal |
| Cinza Claro | `#F5F7F8` | Cards e áreas secundárias |

---

# 🏠 Tela Inicial

A primeira tela deve ser extremamente simples.

```text
+------------------------------------------------+
|                                                |
|              MERCADO REGIONAL                  |
|                                                |
|      Conectando negócios da sua região         |
|                                                |
|                                                |
|      [ Cadastrar Novo Registro ]               |
|                                                |
|      [ Consultar Registros ]                   |
|                                                |
|      [ Gerar Relatórios ]                      |
|                                                |
+------------------------------------------------+
```

### Diretrizes

- Sem dashboard
- Sem gráficos
- Sem tabelas
- Sem excesso de informações
- Apenas ações principais

---

# 📐 Estrutura do Layout

## Header

```text
+------------------------------------------------+
| LOGO           Mercado Regional          Perfil|
+------------------------------------------------+
```

### CSS

```css
background: #35495e;
color: white;
```

---

# 📄 Área Principal

```css
background: #ffffff;
max-width: 900px;
margin: auto;
```

### Características

- Conteúdo centralizado
- Bastante espaço em branco
- Navegação simples
- Foco na tarefa principal do usuário

---

# 🔘 Botões Principais

```css
background: #42b883;
color: white;
border-radius: 12px;
height: 60px;
font-weight: 600;
```

### Hover

```css
background: #347474;
```

---

# 📝 Tela de Cadastro

Evite formulários longos.

Utilize um fluxo em etapas (Wizard).

## Passo 1

```text
O que deseja registrar?

○ Produto
○ Venda
○ Compra
○ Cliente
○ Fornecedor

[ Próximo ]
```

---

## Passo 2

```text
Nome

[________________]
```

---

## Passo 3

```text
Quantidade

[-] 10 [+]
```

---

## Passo 4

```text
Valor

R$ [________]
```

---

## Passo 5

```text
Resumo

Nome: Açaí

Quantidade: 10

Valor: R$ 250,00

[ Salvar Registro ]
```

---

# 🧭 Navegação

Apenas quatro menus principais.

```text
🏠 Início

📝 Cadastros

📋 Registros

📊 Relatórios
```

---

# 🗂️ Estilo dos Cards

```css
background: white;
border-radius: 16px;
box-shadow: 0 4px 20px rgba(0,0,0,.08);
padding: 24px;
```

---

# 🔤 Tipografia

## Fonte Principal

```html
Poppins
```

### Alternativa

```html
Inter
```

### CSS

```css
font-family: 'Poppins', sans-serif;
```

---

# 🏷️ Conceito de Logo

### Opção 1

```text
🛒 Mercado Regional
```

### Opção 2

```text
🌿 Mercado Regional
```

### Opção 3

```text
📍 Mercado Regional
```

### Objetivo da Marca

Representar:

- Comércio local
- Agricultura familiar
- Pesca artesanal
- Pequenos empreendedores
- Economia regional
- Desenvolvimento sustentável

---

# 🏗️ Estrutura Completa do MVP

```text
LOGIN

│
├── INÍCIO
│
├── CADASTRAR
│     ├── Produto
│     ├── Venda
│     ├── Compra
│     ├── Cliente
│     └── Fornecedor
│
├── REGISTROS
│
├── RELATÓRIOS
│
└── PERFIL
```

---

# 🎯 Princípios de UX

## Regra Principal

**O usuário nunca deve enfrentar mais de uma decisão por tela.**

### Para usuários com pouca experiência em informática:

- Botões grandes
- Ícones intuitivos
- Poucos menus
- Linguagem simples
- Processo guiado passo a passo
- Campos bem identificados
- Feedback visual após cada ação

---

# 📱 Conceito Final

O **Mercado Regional** deve transmitir:

- Simplicidade
- Confiança