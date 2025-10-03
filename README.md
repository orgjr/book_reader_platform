# 📚 Book Reader Platform

Uma plataforma web para gerenciamento de livros, autores e leitores, desenvolvida com Django e TailwindCSS.

## 🎯 Sobre o Projeto

O Book Reader Platform é uma aplicação web que permite gerenciar um catálogo de livros, autores e leitores, além de rastrear o histórico de leitura e avaliações. A plataforma oferece uma interface moderna e responsiva para visualização e administração de conteúdo literário.

## ✨ Funcionalidades

- 📖 Gerenciamento de livros com capas e arquivos
- ✍️ Cadastro de autores com biografias e fotos
- 👥 Registro de leitores e suas preferências
- 📊 Sistema de avaliações e histórico de leitura
- 🎨 Interface moderna e responsiva com TailwindCSS
- 🔐 Painel administrativo completo do Django

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.x**
- **Django 5.2.7** - Framework web
- **Pillow 11.3.0** - Processamento de imagens
- **SQLite** - Banco de dados (desenvolvimento)

### Frontend
- **TailwindCSS 4.1.14** - Framework CSS
- **HTML5** - Estrutura das páginas

### Ferramentas de Desenvolvimento
- **djhtml 3.0.9** - Formatação de templates Django
- **ruff 0.13.2** - Linter e formatador Python

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- Python 3.8 ou superior
- Node.js 14 ou superior
- npm ou yarn
- Git

## 🚀 Instalação e Configuração

### 1. Clone o repositório

```bash
git clone git@github.com:orgjr/book_reader_platform.git
cd book_reader_platform
```

### 2. Configure o ambiente virtual Python

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências Python

```bash
pip install -r requirements.txt
```

### 4. Instale as dependências Node.js

```bash
npm install
```

### 5. Configure o banco de dados

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crie um superusuário

```bash
python manage.py createsuperuser
```

### 7. Compile o TailwindCSS (opcional - para desenvolvimento)

Em um terminal separado, execute:

```bash
npm run watch:css
```

Este comando irá monitorar alterações nos arquivos CSS e recompilar automaticamente.

### 8. Inicie o servidor de desenvolvimento

```bash
python manage.py runserver
```

A aplicação estará disponível em: `http://127.0.0.1:8000/`

## 📁 Estrutura do Projeto

```
book_reader_platform/
├── core/                          # Aplicação principal
│   ├── migrations/                # Migrações do banco de dados
│   ├── static/                    # Arquivos estáticos
│   │   └── core/
│   │       └── css/
│   │           ├── input.css      # CSS de entrada do Tailwind
│   │           └── output.css     # CSS compilado
│   ├── templates/                 # Templates HTML
│   │   └── core/
│   │       ├── index.html
│   │       ├── cards.html
│   │       ├── author.html
│   │       ├── book.html
│   │       ├── reader.html
│   │       └── read.html
│   ├── admin.py                   # Configuração do admin
│   ├── models.py                  # Modelos de dados
│   ├── views.py                   # Views da aplicação
│   └── urls.py                    # Rotas da aplicação
├── media/                         # Arquivos de mídia (uploads)
│   ├── images/                    # Imagens (capas, fotos)
│   └── docs/                      # Documentos (PDFs, etc)
├── ty_p/                          # Configurações do projeto
│   ├── settings.py                # Configurações principais
│   ├── urls.py                    # URLs principais
│   └── wsgi.py                    # WSGI config
├── manage.py                      # Script de gerenciamento Django
├── requirements.txt               # Dependências Python
├── package.json                   # Dependências Node.js
└── README.md                      # Este arquivo
```

## 🗄️ Modelos de Dados

### Author (Autor)
- `name`: Nome do autor
- `age`: Idade
- `biography`: Biografia (máx. 200 caracteres)
- `picture`: Foto do autor

### Book (Livro)
- `title`: Título do livro
- `description`: Descrição (máx. 200 caracteres)
- `style`: Estilo/gênero literário
- `cover`: Capa do livro
- `file`: Arquivo do livro (PDF, EPUB, etc)
- `author`: Relação com Author (ForeignKey)

### Reader (Leitor)
- `name`: Nome do leitor
- `age`: Idade
- `preference`: Preferências de leitura
- `books`: Livros lidos (ManyToMany através de Read)

### Read (Leitura)
- `reader`: Relação com Reader (ForeignKey)
- `book`: Relação com Book (ForeignKey)
- `read_date`: Data da leitura
- `evaluation`: Avaliação (nota)

## 🔧 Comandos Úteis

### Django

```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Executar servidor de desenvolvimento
python manage.py runserver

# Abrir shell do Django
python manage.py shell

# Coletar arquivos estáticos (produção)
python manage.py collectstatic
```

### TailwindCSS

```bash
# Compilar CSS em modo watch (desenvolvimento)
npm run watch:css

# Compilar CSS uma vez
npx @tailwindcss/cli -i ./core/static/core/css/input.css -o ./core/static/core/css/output.css
```

### Formatação de Código

```bash
# Formatar código Python com ruff
ruff check --fix .

# Formatar templates Django com djhtml
djhtml core/templates/
```

## 🌐 URLs Disponíveis

- `/` - Página inicial (Top 3 do mês)
- `/author` - Página de autores
- `/book` - Página de livros
- `/reader` - Página de leitores
- `/read` - Página de leitura
- `/admin/` - Painel administrativo

## 🔐 Painel Administrativo

Acesse o painel administrativo em `http://127.0.0.1:8000/admin/` usando as credenciais do superusuário criado.

No painel você pode:
- Gerenciar autores, livros, leitores e leituras
- Fazer upload de capas e arquivos
- Visualizar e editar todos os registros
- Buscar e filtrar dados

## 📝 Configurações Importantes

### Arquivos de Mídia

Os arquivos de mídia (imagens e documentos) são armazenados em:
- **MEDIA_ROOT**: `BASE_DIR / 'media'`
- **MEDIA_URL**: `'media/'`

### Arquivos Estáticos

Os arquivos estáticos são servidos de:
- **STATIC_URL**: `'static/'`
- **STATICFILES_DIRS**: `[BASE_DIR / 'core' / 'static']`

### Internacionalização

- **LANGUAGE_CODE**: `'pt-br'`
- **TIME_ZONE**: `'America/Sao_Paulo'`

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👨‍💻 Autor

Desenvolvido por [orgjr](https://github.com/orgjr)

## 🐛 Problemas Conhecidos

Se encontrar algum problema, por favor abra uma issue no GitHub.

## 📞 Suporte

Para suporte, abra uma issue no repositório do GitHub.

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no GitHub!
