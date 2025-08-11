"""
Classe base para conversores de PDF para Markdown
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

class BaseConverter(ABC):
    """Classe base abstrata para conversores de PDF"""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.available = False
        self.error = None
        
    @abstractmethod
    def is_available(self) -> bool:
        """Verifica se o conversor está disponível"""
        pass
    
    @abstractmethod
    def convert(self, file_content: bytes, filename: str) -> Dict[str, Any]:
        """Converte o PDF para Markdown"""
        pass
    
    def get_status(self) -> Dict[str, Any]:
        """Retorna o status do conversor"""
        return {
            "name": self.name,
            "description": self.description,
            "available": self.available,
            "error": self.error
        }
    
    def __str__(self) -> str:
        return f"{self.name}: {self.description} ({'Disponível' if self.available else 'Não disponível'})"
