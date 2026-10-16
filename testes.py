import unittest

from equipamentos import Equipamento, Servidor, Impressora, criar_equipamento
from ativos import TipoAtivo


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


if __name__ == "__main__":
    unittest.main()