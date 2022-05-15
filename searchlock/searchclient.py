import requests
import json

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, authTok):
        self.authTok = authTok

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.authTok
        return r.headers

class Client():
    def __init__(self):
        self.api = "https://searchlock.me/api/v1/"

    #Colocar sua chave de acesso do Searchlock
    def key(self, authkey):
        self.token = authkey

        #Base Searchlock
        #https://searchlock.me/api/v1/SEARCHLOCK/cpf/	
    def searchlock_cpf(self, cpf):
        re = requests.get(f"{self.api}/SEARCHLOCK/cpf/{cpf}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #https://searchlock.me/api/v1/searchlock/cep/
    def searchlock_cep(self, cep):
        re = requests.get(f"{self.api}/SEARCHLOCK/cep/{cep}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #https://searchlock.me/api/v1/SEARCHLOCK/telefone/
    def searchlock_tel(self, num):
        re = requests.get(f"{self.api}/SEARCHLOCK/telefone/{num}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #https://searchlock.me/api/v1/SEARCHLOCK/email/
    def searchlock_email(self, email):
        re = requests.get(f"{self.api}/SEARCHCLOCK/email/{email}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #https://searchlock.me/api/v1/SEARCHLOCK/placa/
    def searchlock_placa(self, placa):
        re = requests.get(f"{self.api}/SEARCHLOCK/placa/{placa}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #https://searchlock.me/api/v1/SEARCHLOCK/chassis/
    def searchlock_chassi(self, chassi):
        re = requests.get(f"{self.api}/SEARCHLOCK/chassis/{chassi}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #https://searchlock.me/api/v1/SEARCHLOCK/renavam/
    def searchlock_renavam(self, renavam):
        re = requests.get(f"{self.api}/SEARCHLOCK/renavam/{renavam}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj
    
        #https://searchlock.me/api/v1/searchlock/nome/
    def searchlock_nome(self, nome):
        re = requests.get(f"{self.api}/searchlock/nome/{nome}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #Base Shitbroker
        #https://searchlock.me/api/v1/SHIFTBROKER/telefone/
    def shitbroker_tel(self, num):
        re = requests.get(f"{self.api}/SHITBROKER/telefone/{num}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #https://searchlock.me/api/v1/SHIFTBROKER/email/
    def shitbroker_email(self, email):
        re = requests.get(f"{self.api}/SHITBROKER/email/{email}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #https://searchlock.me/api/v1/SHIFTBROKER/nome/
    def shitbroker_nome(self, nome):
        re = requests.get(f"{self.api}/SHITBROKER/nome/{nome}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #https://searchlock.me/api/v1/SHIFTBROKER/cnpj/
    def shitbroker_cnpj(self, cnpj):
        re = requests.get(f"{self.api}/SHITBROKER/cnpj/{cnpj}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #https://searchlock.me/api/v1/SHIFTBROKER/cpf/
    def shitbroker_cpf(self, cpf):
        re = requests.get(f"{self.api}/SHITBROKER/cpf/{cpf}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #Base bigplus
        #https://searchlock.me/api/v1/BIG%20PLUS/cpf/	
    def bigplus_cpf(self, cpf):
        re = requests.get(f"{self.api}/BIG%20PLUS/cpf/{cpf}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj 

        #Base CADMASTER
        #https://searchlock.me/api/v1/CADMASTER/cns/
    def cadmaster_cns(self, cns):
        re = requests.get(f"{self.api}/CADMASTER/cns/{cns}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #https://searchlock.me/api/v1/CADMASTER/cpf/	
    def cadmaster_cpf(self, cpf):
        re = requests.get(f"{self.api}/CADMASTER/cpf/{cpf}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #Base Credivip
        #https://searchlock.me/api/v1/CREDIVIP/cpf/
    def credivip_cpf(self, cpf):
        re = requests.get(f"{self.api}/CREDIVIP/cpf/{cpf}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj
    
        #https://searchlock.me/api/v1/CREDIVIP/cnpj/
    def credivip_cnpj(self, cnpj):
        re = requests.get(f"{self.api}/CREDIVIP/cnpj/{cnpj}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #https://searchlock.me/api/v1/CREDIVIP/telefone/
    def credivip_tel(self, num):
        re = requests.get(f"{self.api}/CREDIVIP/telefone/{num}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj
    
        #https://searchlock.me/api/v1/CREDIVIP/cep/
    def credivip_cep(self, cep):
        re = requests.get(f"{self.api}/CREDIVIP/cep/{cep}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #https://searchlock.me/api/v1/CREDIVIP/nome/
    def credivip_nome(self, nome):
        re = requests.get(f"{self.api}/CREDIVIP/nome{nome}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #https://searchlock.me/api/v1/CREDIVIP/endere%C3%A7o/
    def credivip_enderco(self, endereco):
        re = requests.get(f"{self.api}/CREDIVIP/endere%C3%A7o/{endereco}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #Base Criminal MG
        #https://searchlock.me/api/v1/CRIMINAL%20MG/rg/
    def criminal_mg(self, rg):
        re = requests.get(f"{self.api}/CRIMINAL%20MG/rg/{rg}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #Base E DADOS
        #https://searchlock.me/api/v1/E%20DADOS/cpf/	
    def edados_cpf(self, cpf):
        re = requests.get(f"{self.api}/E%20DADOS/cpf/{cpf}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #Base EMPREGOS PLUS
        #https://searchlock.me/api/v1/EMPREGOS%20PLUS/cpf/
    def empregosplus_cpf(self, cpf):
        re = requests.get(f"{self.api}/EMPREGOS%20PLUS/cpf/{cpf}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj
    
        #https://searchlock.me/api/v1/EMPREGOS%20PLUS/pis/
    def empregosplus_pis(self, pis):
        re = requests.get(f"{self.api}/EMPREGOS%20PLUS/pis/{pis}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #https://searchlock.me/api/v1/EMPREGOS%20PLUS/ctps/
    def empregosplus_ctps(self, ctps):
        re = requests.get(f"{self.api}/EMPREGOS%20PLUS/ctps/{ctps}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #https://searchlock.me/api/v1/EMPREGOS%20PLUS/pasep/
    def empregosplus_pasep(self, pasep):
        re = requests.get(f"{self.api}/EMPREGOS%20PLUS/pasep/{pasep}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #Base Veiculos Lite
        #https://searchlock.me/api/v1/VEICULOS%20LITE/cpf/	
    def veiculoslite_cpf(self, cpf):
        re = requests.get(f"{self.api}/VEICULOS%20LITE/cpf/{cpf}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj
    
        #https://searchlock.me/api/v1/VEICULOS%20LITE/cnh/
    def veiculoslite_cnh(self, cnh):
        re = requests.get(f"{self.api}/VEICLOS%20LITE/cnh/{cnh}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #https://searchlock.me/api/v1/VEICULOS%20LITE/placa/
    def veiculoslite_placa(self, placa):
        re = requests.get(f"{self.api}/VEICULOS%20LITE/placa/{placa}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #https://searchlock.me/api/v1/VEICULOS%20LITE/chassis/
    def veiculoslite_chassi(self, chassi):
        re = requests.get(f"{self.api}/VEICULOS%20LITE/chassis/{chassi}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #https://searchlock.me/api/v1/VEICULOS%20LITE/renavam/
    def veiculoslite_renavam(self, renavam):
        re = requests.get(f"{self.api}/VEICULOS%20LITE/renavam/{renavam}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #https://searchlock.me/api/v1/VEICULOS%20LITE/Individuo/
    def veiculoslite_rg(self, rg):
        re = requests.get(f"{self.api}/VEICULOS%20LITE/Individuo/{rg}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #Base Master
        # https://searchlock.me/api/v1/MASTER/cpf/
    def master_cpf(self, cpf):
        re = requests.get(f"{self.api}/MASTER/cpf/{cpf}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #Base NTBR
        #https://searchlock.me/api/v1/NTBR/cpf/
    def ntbr_cpf(self, cpf):
        re = requests.get(f"{self.api}/NTBR/{cpf}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj
    
        #https://searchlock.me/api/v1/NTBR/cnpj/	
    def ntbr_cnpj(self, cnpj):
        re = requests.get(f"{self.api}/NTBR/cnpj/{cnpj}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj
    
        #https://searchlock.me/api/v1/NTBR/telefone/
    def ntbr_tel(self, num):
        re = requests.get(f"{self.api}/NTBR/telefone/{num}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj
        
        #https://searchlock.me/api/v1/NTBR/cep/
    def ntbr_cep(self, cep):
        re = requests.get(f"{self.api}/NTBR/cep/{cep}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj

        #https://searchlock.me/api/v1/NTBR/nome/
    def ntbr_nome(self, nome):
        re = requests.get(f"{self.api}/NTBR/nome/{nome}", auth=BearerAuth(self.token)); dataj = re.json()
        return dataj
