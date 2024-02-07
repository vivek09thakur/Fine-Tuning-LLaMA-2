import requests

class RunLLM: 
    def __init__(self,ngrok_url) -> None:
        self.ngrok_url = ngrok_url
        pass
    
    def get_resposne(self,prompt):
        data = {'key':prompt}
        response = requests.post(self.ngrok_url,json=data)
        return response.text
    
if __name__=='__main__':
    runner = RunLLM("http://b195-35-231-41-208.ngrok-free.app/generate_response")
    while True:
        try:
            prompt = input("\n<user> ")
            response = runner.get_resposne(prompt=prompt)
            print("\n<model>",response)
        except KeyboardInterrupt:
            break