
import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
import config_data as config
load_dotenv()
api_key = os.getenv("DASHSCOPE_API_KEY")

class VectorStoreService:
    def __init__(self,embedding):
        """
        :param embedding:模型嵌入
        """
        self.embedding = embedding
        self.vector_stor = Chroma(
            collection_name = config.collection_name,
            embedding_function=self.embedding,
            persist_directory=config.persist_directory,
        )

    def get_retriever(self):
        """
        返回向量检索器，方便加入chain
        :return:
        """
        return self.vector_stor.as_retriever(
            search_kwargs={"k":config.similarity_threshold}
        )

if __name__ == "__main__":
    from langchain_community.embeddings import DashScopeEmbeddings
    retriever = VectorStoreService(
        DashScopeEmbeddings(model="text-embedding-v2",dashscope_api_key=api_key)).get_retriever()

    res = retriever.invoke("我的体重80斤，尺码推荐")
    print(res)

