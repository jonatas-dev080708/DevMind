"""
Conversor Docling para conversão real de PDF para Markdown
"""

from .base import BaseConverter
from typing import Dict, Any, Optional
import logging
import tempfile
import os

logger = logging.getLogger(__name__)

class DoclingConverter(BaseConverter):
    """Conversor Docling para conversão real de PDFs"""
    
    def __init__(self):
        super().__init__(
            name="Docling Converter",
            description="Conversor real de PDFs usando Docling"
        )
        self.converter = None
        self._initialize()
    
    def _initialize(self):
        """Tenta inicializar o conversor Docling"""
        try:
            logger.info("Tentando importar Docling...")
            from docling.document_converter import DocumentConverter
            logger.info("Docling importado com sucesso, inicializando converter...")
            
            self.converter = DocumentConverter()
            self.available = True
            self.error = None
            logger.info("✅ Docling converter inicializado com sucesso")
            
        except ImportError as e:
            self.error = f"ImportError: {e}"
            logger.warning(f"❌ Docling não disponível - ImportError: {e}")
            logger.info("💡 Para usar Docling, instale com: pip install docling")
            
        except ModuleNotFoundError as e:
            self.error = f"ModuleNotFoundError: {e}"
            logger.warning(f"❌ Módulo Docling não encontrado: {e}")
            logger.info("💡 Para usar Docling, instale com: pip install docling")
            
        except Exception as e:
            self.error = f"Erro inesperado: {e}"
            logger.error(f"❌ Erro inesperado ao inicializar Docling: {e}")
        
        if not self.available:
            logger.warning("⚠️  Docling não disponível, usando fallback")
    
    def is_available(self) -> bool:
        """Verifica se o Docling está disponível"""
        return self.available and self.converter is not None
    
    def convert(self, file_content: bytes, filename: str) -> Dict[str, Any]:
        """Converte PDF para Markdown usando Docling"""
        if not self.is_available():
            raise RuntimeError("Docling não está disponível")
        
        logger.info(f"Convertendo com Docling: {filename}")
        
        try:
            # Salva temporariamente o PDF
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(file_content)
                tmp_path = tmp.name
            
            logger.info(f"Arquivo temporário criado: {tmp_path}")
            
            try:
                # Converte para markdown usando Docling
                doc = self.converter.convert(tmp_path).document
                markdown_content = doc.export_to_markdown()
                
                logger.info(f"Conversão Docling concluída com sucesso para: {filename}")
                
                return {
                    "success": True,
                    "filename": filename,
                    "markdown": markdown_content,
                    "message": "PDF convertido com sucesso usando Docling",
                    "mode": "full",
                    "converter": self.name
                }
                
            finally:
                # Limpa o arquivo temporário
                try:
                    os.unlink(tmp_path)
                    logger.info(f"Arquivo temporário removido: {tmp_path}")
                except Exception as cleanup_error:
                    logger.warning(f"Erro ao remover arquivo temporário: {cleanup_error}")
                    
        except Exception as e:
            logger.error(f"Erro na conversão Docling: {e}")
            raise RuntimeError(f"Falha na conversão Docling: {e}")
    
    def get_detailed_status(self) -> Dict[str, Any]:
        """Retorna status detalhado do conversor"""
        status = self.get_status()
        status.update({
            "converter_instance": "Disponível" if self.converter else "Não disponível",
            "initialization_success": self.available,
            "recommendations": [
                "Use o modo simples para testes" if not self.available else "Docling funcionando perfeitamente",
                "Instale Docling: pip install docling" if not self.available else "Conversão real ativa",
                "Verifique ambiente virtual" if not self.available else "Sistema operacional compatível"
            ]
        })
        return status
