#!/usr/bin/env python3
"""
Conversor PDF simples e eficiente para Markdown
Usa apenas as bibliotecas essenciais: PyPDF2 e pdfplumber
"""

import logging
from typing import Dict, Any, Optional
from pathlib import Path

logger = logging.getLogger(__name__)

class SimplePDFConverter:
    """Conversor PDF simples e eficiente para Markdown"""
    
    def __init__(self):
        self.name = "Simple PDF Converter"
        self.description = "Conversor PDF real usando PyPDF2 e pdfplumber"
        self.version = "1.0.0"
        self.available = False
        
        # Tenta importar as dependências
        self._import_dependencies()
    
    def _import_dependencies(self):
        """Importa as dependências necessárias"""
        try:
            import PyPDF2
            import pdfplumber
            self.available = True
            logger.info("✅ Dependências de PDF importadas com sucesso")
        except ImportError as e:
            logger.warning(f"⚠️ Dependências não disponíveis: {e}")
            self.available = False
    
    def convert_pdf(self, pdf_content: bytes, filename: str) -> Dict[str, Any]:
        """
        Converte PDF para Markdown usando bibliotecas essenciais
        
        Args:
            pdf_content: Conteúdo do arquivo PDF em bytes
            filename: Nome do arquivo PDF
            
        Returns:
            Dicionário com o resultado da conversão
        """
        if not self.available:
            return self._fallback_conversion(pdf_content, filename)
        
        try:
            logger.info(f"🔄 Convertendo {filename} usando conversor real")
            
            # Tenta usar pdfplumber primeiro (melhor para extração de texto)
            markdown_content = self._convert_with_pdfplumber(pdf_content)
            
            if markdown_content:
                return {
                    "success": True,
                    "filename": filename,
                    "markdown": markdown_content,
                    "converter_used": self.name,
                    "mode": "real",
                    "pages": self._count_pages(pdf_content),
                    "size_bytes": len(pdf_content)
                }
            
            # Fallback para PyPDF2 se pdfplumber falhar
            markdown_content = self._convert_with_pypdf2(pdf_content)
            
            if markdown_content:
                return {
                    "success": True,
                    "filename": filename,
                    "markdown": markdown_content,
                    "converter_used": f"{self.name} (PyPDF2)",
                    "mode": "real",
                    "pages": self._count_pages(pdf_content),
                    "size_bytes": len(pdf_content)
                }
            
            # Se ambos falharem, usa fallback
            logger.warning("⚠️ Conversores reais falharam, usando fallback")
            return self._fallback_conversion(pdf_content, filename)
            
        except Exception as e:
            logger.error(f"❌ Erro na conversão real: {e}")
            return self._fallback_conversion(pdf_content, filename)
    
    def _convert_with_pdfplumber(self, pdf_content: bytes) -> Optional[str]:
        """Converte usando pdfplumber (melhor qualidade)"""
        try:
            import pdfplumber
            
            with pdfplumber.open(pdf_content) as pdf:
                markdown_lines = []
                
                for page_num, page in enumerate(pdf.pages, 1):
                    # Extrai texto da página
                    text = page.extract_text()
                    if text:
                        # Adiciona cabeçalho da página
                        markdown_lines.append(f"\n## Página {page_num}\n")
                        
                        # Processa o texto
                        processed_text = self._process_text(text)
                        markdown_lines.append(processed_text)
                        
                        # Adiciona separador entre páginas
                        markdown_lines.append("\n---\n")
                
                return "\n".join(markdown_lines)
                
        except Exception as e:
            logger.warning(f"⚠️ pdfplumber falhou: {e}")
            return None
    
    def _convert_with_pypdf2(self, pdf_content: bytes) -> Optional[str]:
        """Converte usando PyPDF2 (fallback)"""
        try:
            import PyPDF2
            from io import BytesIO
            
            pdf_file = BytesIO(pdf_content)
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            markdown_lines = []
            
            for page_num, page in enumerate(pdf_reader.pages, 1):
                # Extrai texto da página
                text = page.extract_text()
                if text:
                    # Adiciona cabeçalho da página
                    markdown_lines.append(f"\n## Página {page_num}\n")
                    
                    # Processa o texto
                    processed_text = self._process_text(text)
                    markdown_lines.append(processed_text)
                    
                    # Adiciona separador entre páginas
                    markdown_lines.append("\n---\n")
            
            return "\n".join(markdown_lines)
            
        except Exception as e:
            logger.warning(f"⚠️ PyPDF2 falhou: {e}")
            return None
    
    def _process_text(self, text: str) -> str:
        """Processa e formata o texto extraído"""
        if not text:
            return ""
        
        # Remove espaços extras e quebras de linha desnecessárias
        lines = text.split('\n')
        processed_lines = []
        
        for line in lines:
            line = line.strip()
            if line:
                # Detecta títulos (linhas em maiúsculo ou com formatação especial)
                if line.isupper() or len(line) < 100 and line.endswith(':'):
                    processed_lines.append(f"### {line}")
                else:
                    processed_lines.append(line)
        
        return "\n\n".join(processed_lines)
    
    def _count_pages(self, pdf_content: bytes) -> int:
        """Conta o número de páginas do PDF"""
        try:
            import PyPDF2
            from io import BytesIO
            
            pdf_file = BytesIO(pdf_content)
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            return len(pdf_reader.pages)
        except:
            return 0
    
    def _fallback_conversion(self, pdf_content: bytes, filename: str) -> Dict[str, Any]:
        """Conversão de fallback quando os conversores reais falham"""
        logger.info(f"📝 Usando conversão de fallback para {filename}")
        
        # Simula conversão básica
        markdown_content = f"""# {filename}

## Conteúdo do PDF

Este arquivo PDF foi processado usando conversão de fallback.

**Informações do arquivo:**
- Nome: {filename}
- Tamanho: {len(pdf_content)} bytes
- Páginas: {self._count_pages(pdf_content)}

**Nota:** Para conversão completa, instale as dependências:
```bash
pip install pypdf2 pdfplumber
```

---
*Conversão realizada em modo fallback*
"""
        
        return {
            "success": True,
            "filename": filename,
            "markdown": markdown_content,
            "converter_used": f"{self.name} (Fallback)",
            "mode": "fallback",
            "pages": self._count_pages(pdf_content),
            "size_bytes": len(pdf_content),
            "note": "Instale pypdf2 e pdfplumber para conversão completa"
        }
    
    def get_status(self) -> Dict[str, Any]:
        """Retorna o status do conversor"""
        return {
            "name": self.name,
            "description": self.description,
            "version": self.version,
            "available": self.available,
            "mode": "real" if self.available else "fallback"
        }
    
    def get_detailed_status(self) -> Dict[str, Any]:
        """Retorna status detalhado do conversor"""
        return {
            "name": self.name,
            "description": self.description,
            "version": self.version,
            "available": self.available,
            "mode": "real" if self.available else "fallback",
            "dependencies": {
                "pypdf2": "PyPDF2 para leitura básica de PDF",
                "pdfplumber": "pdfplumber para extração avançada de texto"
            },
            "capabilities": [
                "Extração de texto de PDFs",
                "Conversão para Markdown",
                "Contagem de páginas",
                "Processamento de múltiplas páginas"
            ]
        }

