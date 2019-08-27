from blockchain import Blockchain


if __name__ == '__main__':
    blockchain = Blockchain()

    blockchain.add_new_block('Primeiro bloco!')



    print(blockchain.get_all())