# 🔧 Guia de Solução de Problemas

## ❌ Problemas Comuns e Soluções

### 1. Erro: "DLL load failed while importing onnxruntime"
**Sintoma:** Erro ao tentar importar Docling no Windows
**Causa:** Incompatibilidade do ONNX Runtime com o sistema Windows
**Solução:**
```bash
# Use o modo simples (recomendado para Windows)
API_MODE=simple

# Ou tente reinstalar as dependências
pip uninstall docling onnxruntime
pip install docling --no-cache-dir
```

### 2. Erro: "ModuleNotFoundError: No module named 'docling'"
**Sintoma:** Módulo Docling não encontrado
**Causa:** Docling não instalado ou ambiente virtual incorreto
**Solução:**
```bash
# Ative o ambiente virtual (se existir)
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Ou instale apenas o Docling
pip install docling
```

### 3. Erro: "ImportError: cannot import name 'DocumentConverter'"
**Sintoma:** Erro ao importar classe específica do Docling
**Causa:** Versão incompatível ou instalação corrompida
**Solução:**
```bash
# Reinstale o Docling
pip uninstall docling
pip install docling==0.1.0

# Verifique a versão
pip show docling
```

### 4. Problemas de Permissão no Windows
**Sintoma:** Erros de acesso negado ou DLL
**Causa:** Restrições de segurança do Windows
**Solução:**
- Execute o PowerShell como Administrador
- Desative temporariamente o Windows Defender
- Use o modo simples (`API_MODE=simple`)

## 🚀 Soluções Rápidas

### Solução 1: Usar Modo Simples (Recomendado para Windows)
```bash
# Edite o arquivo .env
API_MODE=simple

# Reinicie a aplicação
python start.py
```

### Solução 2: Verificar Ambiente Virtual
```bash
# Crie um novo ambiente virtual
python -m venv .venv

# Ative o ambiente
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Instale dependências
pip install -r requirements-simple.txt
```

### Solução 3: Limpar Cache e Reinstalar
```bash
# Limpe o cache do pip
pip cache purge

# Reinstale dependências
pip install -r requirements.txt --force-reinstall
```

## 📋 Verificação de Status

### 1. Verificar se a API está funcionando
```bash
# Acesse no navegador
http://localhost:8000/health
http://localhost:8000/docs
```

### 2. Verificar logs da aplicação
```bash
# Execute com log detalhado
python start.py

# Ou edite .env
LOG_LEVEL=debug
```

### 3. Verificar dependências instaladas
```bash
pip list | grep -E "(fastapi|uvicorn|docling|onnx)"
```

## 🔍 Debugging Avançado

### 1. Logs Detalhados
```python
# No arquivo .env
LOG_LEVEL=debug
```

### 2. Verificar Variáveis de Ambiente
```bash
# No PowerShell
Get-ChildItem Env: | Where-Object {$_.Name -like "*API*"}
```

### 3. Testar Importação Manual
```python
# No Python
python -c "import docling; print('Docling OK')"
```

## 📞 Suporte

Se os problemas persistirem:

1. **Verifique os logs** da aplicação
2. **Use o modo simples** para testes
3. **Consulte a documentação** do Docling
4. **Verifique compatibilidade** do sistema operacional

## ✅ Checklist de Verificação

- [ ] Ambiente virtual ativado
- [ ] Dependências instaladas corretamente
- [ ] Arquivo .env configurado
- [ ] Porta 8000 disponível
- [ ] Permissões adequadas no sistema
- [ ] Logs da aplicação verificados
