DOCUMENTS_NAME = {1:['fiche de paie', 'rapport infra réseau', 'rapport SDN'],
                  2:['rapport Active Directory', 'rapport stockiométrique'],
                  3:['moteur thermique', 'moteur essence', 'moteur diesel',
                     'moteur éléctrique', 'vanne egr', 'turbo']}

class SearchingFiles:
    def searching_files(self, key_words: list[str]):
        result_search = {}

        for machine, files in DOCUMENTS_NAME.items():
            for file_name in files:
                for word in key_words:
                    if word.lower() in file_name.lower():
                        if machine in result_search:
                            result_search[machine].append(file_name)
                        else:
                            files_list = [file_name]
                            result_search[machine] = files_list

        return result_search
