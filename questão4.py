faturamento_mensal = {"SP":67836.47, "RJ": 36678.66,"MG": 29229.88, "ES": 27165.48,
                      "outro":19849.53
                      }

faturamento_total = faturamento_mensal.get("SP") + faturamento_mensal.get("RJ")+faturamento_mensal.get("MG")+faturamento_mensal.get("ES")+faturamento_mensal.get("outro")
porcentagem = ( faturamento_mensal.get("SP")/faturamento_total)*100
print(porcentagem)