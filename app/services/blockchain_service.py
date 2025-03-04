from domain.models.block import Block
import time

class BlockchainService:
    def __init__(self):
        self.chain = [self._create_genesis_block()]

    def _create_genesis_block(self) -> Block:
        return Block(index=0, timestamp=time.time(), data="Genesis Block", previous_hash="0")

    def add_block(self, data: str) -> Block:
        previous_block = self.chain[-1]
        new_block = Block(
            index=len(self.chain),
            timestamp=time.time(),
            data=data,
            previous_hash=previous_block.hash
        )
        self.chain.append(new_block)
        return new_block

    def get_chain(self):
        return self.chain


blockchain_service = BlockchainService()