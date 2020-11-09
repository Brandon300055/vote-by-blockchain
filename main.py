#########################################################################################################
#  _    _                  ______           ______  _             _          _           _
# | |  | |    _           (____  \         (____  \| |           | |        | |         (_)
# | |  | |__ | |_  ____    ____)  )_   _    ____)  ) | ___   ____| |  _ ____| | _   ____ _ ____
#  \ \/ / _ \|  _)/ _  )  |  __  (| | | |  |  __  (| |/ _ \ / ___) | / ) ___) || \ / _  | |  _ \
#   \  / |_| | |_( (/ /   | |__)  ) |_| |  | |__)  ) | |_| ( (___| |< ( (___| | | ( ( | | | | | |
#    \/ \___/ \___)____)  |______/ \__  |  |______/|_|\___/ \____)_| \_)____)_| |_|\_||_|_|_| |_|
#                                  (____/
#                                     By Brandon
#########################################################################################################

from block import Block

blockchain = []

genesis_block = Block("test", [
    "test",
])

vote = Block(genesis_block.block_hash, ["vote for a"])
vote2 = Block(vote.block_hash, ["vote for a"])

# with open('public.txt', 'w') as outfile:
#     json.dump(data, outfile)



print(genesis_block.block_hash)
print(vote.block_hash)
print(vote2.block_hash) #e988be4f7994831209fc907d537d670dc87606cbed1ae5ee7ce0f313c64bb36d