import axios from "axios";

const API_URL = process.env.REACT_APP_FINAL_SEQUENCE_API_URL;
const instance = axios.create({
  baseURL: API_URL
});

instance.defaults.headers.post["Content-Type"] =
  "application/json; charset=utf-8";

class LivingProofAPI {
  static async fetchLivingProofList() {
    const response = await instance.get("/living-proofs");
    return response.data;
  }

  static async fetchLivingProofDetail(id) {
    const response = await instance.get(`/living-proofs/${id}`);
    return response.data;
  }

  static async fetchTodoList(id){
    const response = await instance.get(`/todo-list/${id}`);
    return response.data
  }

  static async postTodoList(id,param){
    const response = await instance.post(`/todo-list/${id}`,param);
    return response.data
  }

  static async deleteTodo(id,todoId){
    const response = await instance.delete(`/todo-list/${id}/${todoId}`);
    return response.data
  }

  static async modifyTodo(id,todoId,param){
    const response = await instance.put(`/todo-list/${id}/${todoId}`,param);
    return response.data
  }
}

export default LivingProofAPI;
