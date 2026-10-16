import unittest

from equipamentos import Equipamento, Servidor, Impressora, criar_equipamento
from tipos import TipoAtivo
from vulnerabilidades import Vulnerabilidade


class TestEquipamento(unittest.TestCase):
    def test_cria_equipamento_valido(self):
        e = Equipamento(1, "  Servidor DNS ", "Maria Silva", "Datacenter")
        self.assertEqual(e.nome, "Servidor DNS")  # espaços removidos

    def test_id_invalido(self):
        for ruim in (0, -3, "7", None):
            with self.assertRaises(ValueError):
                Equipamento(ruim, "Nome", "Maria", "Sala 1")

    def test_nome_so_numeros(self):
        with self.assertRaises(ValueError):
            Equipamento(1, "123", "Maria", "Sala 1")

    def test_responsavel_com_numero(self):
        with self.assertRaises(ValueError):
            Equipamento(1, "Nome", "Maria2", "Sala 1")


class TestarSubclasses(unittest.TestCase):
    def test_fabrica_cria_subclasse_certa(self):
        e = criar_equipamento(TipoAtivo.SERVIDOR, 1, "DNS", "Maria", "Datacenter")
        self.assertIsInstance(e, Servidor)
        self.assertIsInstance(e, Equipamento)

    def test_fator_de_exposicao_polimorfico(self):
        s = Servidor(1, "DNS", "Maria", "Datacenter")
        i = Impressora(2, "HP", "Maria", "Recepção")
        self.assertGreater(s.fator_exposicao, i.fator_exposicao)

    def test_to_dict(self):
        s = Servidor(1, "DNS", "Maria", "Datacenter")
        self.assertEqual(s.to_dict()["tipo"], 3)


class TestVulnerabilidade(unittest.TestCase):
    def test_classificacao_cvss(self):
        casos = {0: "nenhuma", 3.9: "baixa", 4: "média", 7: "alta", 9.8: "crítica"}
        for nota, esperado in casos.items():
            self.assertEqual(Vulnerabilidade(1, "x", "y", nota).classificacao, esperado)

    def test_severidade_fora_da_faixa(self):
        for ruim in (-1, 10.1, "abc", None):
            with self.assertRaises(ValueError):
                Vulnerabilidade(1, "x", "y", ruim)

    def test_associar_duplicado(self):
        v = Vulnerabilidade(1, "x", "y", 5)
        v.associar(3)
        with self.assertRaises(ValueError):
            v.associar(3)

    def test_descricao_vazia(self):
        with self.assertRaises(ValueError):
            Vulnerabilidade(1, "   ", "y", 5)
        

if __name__ == "__main__":
    unittest.main()