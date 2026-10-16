import unittest

from equipamentos import Equipamento


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


if __name__ == "__main__":
    unittest.main()