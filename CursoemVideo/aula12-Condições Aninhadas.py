prof = str(input('\033[1;34mQual a sua Profissão?: ')).strip()
if prof.lower() in 'médico enfermeiro bombeiro dentista':
    print(f'\033[1;33mSua profissão de {prof.capitalize()} tem em foco cuidar e salvar as pessoas!!')
elif prof.lower() == 'mecânico' or prof.lower() == 'engenheiro':
    print(f'\033[1;31mEssa profissão de {prof.capitalize()} facilitam o dia a dia \ne fazem manuntenção de objetos tecnológicos!!!')
elif prof.lower() in 'ator atriz dançarino bailarina bailarino':
    print(f'\033[1;36msua profissão de {prof.capitalize()} é algo artístico!!!')
else:
    print(f'Ainda não catálogamos {prof.capitalize()} em nosso sistema, desculpe!!!')
