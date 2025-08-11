#!/usr/bin/env python3
"""
API simplificada para converter PDFs em Markdown (versão de teste)
Esta versão simula a conversão para testar a estrutura da API
"""

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import tempfile
import os
import logging
from typing import Optional
import uvicorn

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="PDF to Markdown Converter (Teste)",
    description="API para converter PDFs em Markdown - Versão de teste",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "message": "PDF to Markdown Converter API (Teste)",
        "status": "running",
        "note": "Esta é uma versão de teste que simula a conversão"
    }

@app.post("/convert-pdf")
async def convert_pdf(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="Nome do arquivo não fornecido")
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Arquivo deve ser um PDF")
    
    try:
        content = await file.read()
        if not content:
            raise HTTPException(status_code=400, detail="Arquivo vazio")

        # Simula o processamento do arquivo
        logger.info(f"Arquivo recebido: {file.filename} ({len(content)} bytes)")
        
        # Simula a conversão (mock)
        mock_markdown = f"""# Documento convertido: {file.filename}

Este é um exemplo de markdown convertido do PDF.

## Informações do arquivo:
- **Nome original**: {file.filename}
- **Tamanho**: {len(content)} bytes
- **Tipo**: PDF

## Conteúdo simulado:
Este é um conteúdo de exemplo que simula a conversão real do PDF para Markdown.

### Seções simuladas:
1. **Introdução**: Texto de exemplo
2. **Desenvolvimento**: Mais conteúdo simulado
3. **Conclusão**: Final do documento

---
*Nota: Esta é uma versão de teste. A conversão real seria feita pelo Docling.*
"""
        
        logger.info(f"Conversão simulada concluída para: {file.filename}")
        return {
            "success": True,
            "filename": file.filename,
            "markdown": mock_markdown,
            "message": "PDF convertido com sucesso (simulação)",
            "note": "Esta é uma versão de teste"
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro inesperado: {e}")
        raise HTTPException(status_code=500, detail=f"Erro interno do servidor: {str(e)}")

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "mode": "test",
        "timestamp": "2024-01-01T00:00:00Z",
        "note": "API funcionando em modo de teste"
    }

if __name__ == "__main__":
    uvicorn.run(
        "main-simple:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

