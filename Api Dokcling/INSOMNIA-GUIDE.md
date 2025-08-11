# 🎯 Guia Completo - Testando a API no Insomnia

## 📋 Pré-requisitos

1. ✅ API rodando em `http://localhost:8000`
2. ✅ Insomnia instalado
3. ✅ Arquivo PDF para teste

## 🚀 Configuração Rápida (Importar)

### Opção 1: Importar Configuração
1. Abra o Insomnia
2. Clique em **Import/Export** (ícone de engrenagem)
3. Selecione **Import Data**
4. Escolha **From File**
5. Selecione o arquivo `insomnia-config.json`
6. Clique em **Import**

### Opção 2: Configuração Manual
Siga os passos abaixo para criar manualmente.

## 🔧 Configuração Manual

### 1. Criar Workspace
- Clique em **New Workspace**
- Nome: `PDF to Markdown API`
- Descrição: `API para converter PDFs em Markdown`

### 2. Criar Environment
- Clique em **Manage Environments**
- Clique em **New Environment**
- Nome: `Local Environment`
- Adicione variável:
  - **Name**: `base_url`
  - **Value**: `http://localhost:8000`
- Salve o environment

### 3. Criar Requests

#### **Request 1: Status da API**
- **Método**: GET
- **URL**: `{{ _.base_url }}/`
- **Nome**: `GET / - Status da API`
- **Descrição**: Endpoint raiz para verificar o status da API

#### **Request 2: Health Check**
- **Método**: GET
- **URL**: `{{ _.base_url }}/health`
- **Nome**: `GET /health - Health Check`
- **Descrição**: Endpoint para verificação de saúde da aplicação

#### **Request 3: Converter PDF**
- **Método**: POST
- **URL**: `{{ _.base_url }}/convert-pdf`
- **Nome**: `POST /convert-pdf - Converter PDF`
- **Descrição**: Endpoint para converter PDF em Markdown
- **Body**: 
  - Selecione **Form**
  - Adicione campo:
    - **Key**: `file`
    - **Type**: `File`
    - **Value**: Selecione um arquivo PDF

## 🧪 Testando os Endpoints

### **1. Teste GET /**
- Clique em **Send**
- **Resposta esperada**:
```json
{
  "message": "PDF to Markdown Converter API",
  "status": "running",
  "docling_available": false,
  "mode": "simple"
}
```

### **2. Teste GET /health**
- Clique em **Send**
- **Resposta esperada**:
```json
{
  "status": "healthy",
  "docling_available": false,
  "mode": "simple",
  "timestamp": "2024-01-01T00:00:00Z"
}
```

### **3. Teste POST /convert-pdf**
- Selecione um arquivo PDF no campo `file`
- Clique em **Send**
- **Resposta esperada**:
```json
{
  "success": true,
  "filename": "seu-arquivo.pdf",
  "markdown": "# Documento convertido: seu-arquivo.pdf\n\n...",
  "message": "PDF convertido com sucesso (modo simples)",
  "mode": "simple"
}
```

## 🔍 Troubleshooting

### **Erro: "Connection refused"**
- ✅ Verifique se a API está rodando: `python start.py`
- ✅ Confirme a porta: `http://localhost:8000`

### **Erro: "Request failed"**
- ✅ Verifique se o arquivo PDF é válido
- ✅ Confirme se o campo `file` está configurado como `File`

### **Erro: "Invalid URL"**
- ✅ Verifique se o environment está selecionado
- ✅ Confirme se a variável `base_url` está definida

### **Resposta vazia**
- ✅ Verifique os logs da API no terminal
- ✅ Confirme se a API está respondendo

## 📱 Dicas do Insomnia

### **1. Auto-complete**
- Use `{{ _.base_url }}` para URLs baseadas no environment
- Use `{{ _.base_url }}/health` para endpoints específicos

### **2. Headers Automáticos**
- O Insomnia adiciona automaticamente `Content-Type` para multipart/form-data
- Não é necessário configurar headers manualmente para esta API

### **3. Histórico de Requests**
- O Insomnia mantém histórico de todas as requisições
- Útil para debug e comparação de respostas

### **4. Exportar Respostas**
- Clique com botão direito na resposta
- Selecione **Export Response**
- Salve como arquivo para análise

## 🎯 Próximos Passos

1. **Teste todos os endpoints** para confirmar funcionamento
2. **Teste com diferentes PDFs** para validar comportamento
3. **Explore a documentação Swagger** em `http://localhost:8000/docs`
4. **Integre com n8n** usando os endpoints testados

## 📞 Suporte

Se encontrar problemas:
1. Verifique se a API está rodando
2. Confirme as configurações do Insomnia
3. Teste com `python test_api.py`
4. Verifique os logs da API no terminal

