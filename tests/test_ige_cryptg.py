import os
import random
import unittest
import pyaesni
import cryptg


class TestIGEPyaesniCryptg(unittest.TestCase):
    DATA_CHUNK_MAX_SIZE = 64
    KEY_SIZE = 32
    IV_SIZE = 32

    TESTS_AMOUNT = 500

    TEMPLATE = """
    def test_ige_with_cryptg_{mode1}_{count}(self):
        data = {data}
        key = {key}
        iv = {iv}

        a = pyaesni.ige256_{mode1}(data, key, iv)
        b = cryptg.{mode2}_ige(a, key, iv)

        self.assertEqual(data, b)
    """.replace("\n    ", "\n")

    for count in range(TESTS_AMOUNT):
        exec(
            TEMPLATE.format(
                mode1="encrypt",
                mode2="decrypt",
                count=count,
                data=os.urandom(random.randint(1, DATA_CHUNK_MAX_SIZE) * 16),
                key=os.urandom(KEY_SIZE),
                iv=os.urandom(IV_SIZE),
            )
        )

    for count in range(TESTS_AMOUNT):
        exec(
            TEMPLATE.format(
                mode1="decrypt",
                mode2="encrypt",
                count=count,
                data=os.urandom(random.randint(1, DATA_CHUNK_MAX_SIZE) * 16),
                key=os.urandom(KEY_SIZE),
                iv=os.urandom(IV_SIZE),
            )
        )


if __name__ == "__main__":
    unittest.main()
