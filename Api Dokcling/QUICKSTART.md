# 🚀 Início Rápido - API PDF to Markdown

## ⚡ Execução em 3 Passos

### 1. Instalar dependências básicas
```bash
pip install -r requirements-simple.txt
```

### 2. Criar arquivo de configuração
```bash
copy env.example .env
```

### 3. Executar a API
```bash
python start.py
```

## 🌐 Acessar a API

- **API**: http://localhost:8000
- **Documentação**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## 🧪 Testar

Em outro terminal:
```bash
python test_api.py
```

## 📝 Converter PDF

Use a documentação Swagger em http://localhost:8000/docs ou faça uma requisição POST para `/convert-pdf`.

## ✅ Status

Se tudo estiver funcionando, você verá:
- ✅ API rodando na porta 8000
- ✅ Modo: simple (teste)
- ✅ Documentação disponível
- ✅ Health check funcionando

## 🔧 Problemas Comuns

**Erro de conexão**: Verifique se a API está rodando
**Erro de dependências**: Use `requirements-simple.txt` em vez de `requirements.txt`
**Porta ocupada**: Mude a porta no arquivo `.env`

## 📚 Próximos Passos

1. Teste a conversão de PDFs
2. Explore a documentação Swagger
3. Integre com n8n ou outras ferramentas
4. Para conversão real, configure o modo completo
