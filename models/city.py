from jethive.model import Model
from jethive.models.country import Country


class City(Model):
    c_name = str
    c_country = Country
    
    @classmethod
    def seed(cls):
        return [
            {'name': 'Kabul', 'country_id': Country.pick.with_name('Afghanistan').id},
            {'name': 'Herat', 'country_id': Country.pick.with_name('Afghanistan').id},
            {'name': 'Mazar-i-Sharif', 'country_id': Country.pick.with_name('Afghanistan').id},
            {'name': 'Kandahar', 'country_id': Country.pick.with_name('Afghanistan').id},
            {'name': 'Jalalabad', 'country_id': Country.pick.with_name('Afghanistan').id},
            {'name': 'Lashkargah', 'country_id': Country.pick.with_name('Afghanistan').id},

            {'name': 'Tirana', 'country_id': Country.pick.with_name('Albania').id},
            {'name': 'Durrës', 'country_id': Country.pick.with_name('Albania').id},
            {'name': 'Vlorë', 'country_id': Country.pick.with_name('Albania').id},
            {'name': 'Shkodër', 'country_id': Country.pick.with_name('Albania').id},
            {'name': 'Fier', 'country_id': Country.pick.with_name('Albania').id},

            {'name': 'Algiers', 'country_id': Country.pick.with_name('Algeria').id},
            {'name': 'Oran', 'country_id': Country.pick.with_name('Algeria').id},
            {'name': 'Constantine', 'country_id': Country.pick.with_name('Algeria').id},
            {'name': 'Batna', 'country_id': Country.pick.with_name('Algeria').id},
            {'name': 'Annaba', 'country_id': Country.pick.with_name('Algeria').id},
            {'name': 'Tlemcen', 'country_id': Country.pick.with_name('Algeria').id},

            {'name': 'Andorra la Vella', 'country_id': Country.pick.with_name('Andorra').id},
            {'name': 'Escaldes-Engordany', 'country_id': Country.pick.with_name('Andorra').id},
            {'name': 'Encamp', 'country_id': Country.pick.with_name('Andorra').id},
            {'name': 'La Massana', 'country_id': Country.pick.with_name('Andorra').id},

            {'name': 'Luanda', 'country_id': Country.pick.with_name('Angola').id},
            {'name': 'Lobito', 'country_id': Country.pick.with_name('Angola').id},
            {'name': 'Huambo', 'country_id': Country.pick.with_name('Angola').id},
            {'name': 'Benguela', 'country_id': Country.pick.with_name('Angola').id},
            {'name': 'Kuito', 'country_id': Country.pick.with_name('Angola').id},
            {'name': 'Malanje', 'country_id': Country.pick.with_name('Angola').id},

            {'name': 'St. John\'s', 'country_id': Country.pick.with_name('Antigua and Barbuda').id},
            {'name': 'All Saints', 'country_id': Country.pick.with_name('Antigua and Barbuda').id},
            {'name': 'Liberta', 'country_id': Country.pick.with_name('Antigua and Barbuda').id},
            {'name': 'Bolans', 'country_id': Country.pick.with_name('Antigua and Barbuda').id},

            {'name': 'Buenos Aires', 'country_id': Country.pick.with_name('Argentina').id},
            {'name': 'Córdoba', 'country_id': Country.pick.with_name('Argentina').id},
            {'name': 'Rosario', 'country_id': Country.pick.with_name('Argentina').id},
            {'name': 'Mendoza', 'country_id': Country.pick.with_name('Argentina').id},
            {'name': 'San Miguel de Tucumán', 'country_id': Country.pick.with_name('Argentina').id},
            {'name': 'La Plata', 'country_id': Country.pick.with_name('Argentina').id},

            {'name': 'Yerevan', 'country_id': Country.pick.with_name('Armenia').id},
            {'name': 'Gyumri', 'country_id': Country.pick.with_name('Armenia').id},
            {'name': 'Vanadzor', 'country_id': Country.pick.with_name('Armenia').id},
            {'name': 'Vagharshapat', 'country_id': Country.pick.with_name('Armenia').id},
            {'name': 'Hrazdan', 'country_id': Country.pick.with_name('Armenia').id},
            {'name': 'Abovyan', 'country_id': Country.pick.with_name('Armenia').id},

            {'name': 'Sydney', 'country_id': Country.pick.with_name('Australia').id},
            {'name': 'Melbourne', 'country_id': Country.pick.with_name('Australia').id},
            {'name': 'Brisbane', 'country_id': Country.pick.with_name('Australia').id},
            {'name': 'Perth', 'country_id': Country.pick.with_name('Australia').id},
            {'name': 'Adelaide', 'country_id': Country.pick.with_name('Australia').id},
            {'name': 'Gold Coast', 'country_id': Country.pick.with_name('Australia').id},

            {'name': 'Vienna', 'country_id': Country.pick.with_name('Austria').id},
            {'name': 'Graz', 'country_id': Country.pick.with_name('Austria').id},
            {'name': 'Linz', 'country_id': Country.pick.with_name('Austria').id},
            {'name': 'Salzburg', 'country_id': Country.pick.with_name('Austria').id},
            {'name': 'Innsbruck', 'country_id': Country.pick.with_name('Austria').id},
            {'name': 'Klagenfurt', 'country_id': Country.pick.with_name('Austria').id},

            {'name': 'Baku', 'country_id': Country.pick.with_name('Azerbaijan').id},
            {'name': 'Ganja', 'country_id': Country.pick.with_name('Azerbaijan').id},
            {'name': 'Sumgait', 'country_id': Country.pick.with_name('Azerbaijan').id},
            {'name': 'Mingachevir', 'country_id': Country.pick.with_name('Azerbaijan').id},
            {'name': 'Lankaran', 'country_id': Country.pick.with_name('Azerbaijan').id},
            {'name': 'Nakhchivan', 'country_id': Country.pick.with_name('Azerbaijan').id},

            {'name': 'Nassau', 'country_id': Country.pick.with_name('Bahamas').id},
            {'name': 'Lucaya', 'country_id': Country.pick.with_name('Bahamas').id},
            {'name': 'Freeport', 'country_id': Country.pick.with_name('Bahamas').id},
            {'name': 'George Town', 'country_id': Country.pick.with_name('Bahamas').id},

            {'name': 'Manama', 'country_id': Country.pick.with_name('Bahrain').id},
            {'name': 'Riffa', 'country_id': Country.pick.with_name('Bahrain').id},
            {'name': 'Muharraq', 'country_id': Country.pick.with_name('Bahrain').id},
            {'name': 'Hamad Town', 'country_id': Country.pick.with_name('Bahrain').id},

            {'name': 'Dhaka', 'country_id': Country.pick.with_name('Bangladesh').id},
            {'name': 'Chittagong', 'country_id': Country.pick.with_name('Bangladesh').id},
            {'name': 'Khulna', 'country_id': Country.pick.with_name('Bangladesh').id},
            {'name': 'Rajshahi', 'country_id': Country.pick.with_name('Bangladesh').id},
            {'name': 'Comilla', 'country_id': Country.pick.with_name('Bangladesh').id},
            {'name': 'Barisal', 'country_id': Country.pick.with_name('Bangladesh').id},

            {'name': 'Bridgetown', 'country_id': Country.pick.with_name('Barbados').id},
            {'name': 'Speightstown', 'country_id': Country.pick.with_name('Barbados').id},
            {'name': 'Oistins', 'country_id': Country.pick.with_name('Barbados').id},
            {'name': 'Bathsheba', 'country_id': Country.pick.with_name('Barbados').id},
            {'name': 'Holetown', 'country_id': Country.pick.with_name('Barbados').id},

            {'name': 'Minsk', 'country_id': Country.pick.with_name('Belarus').id},
            {'name': 'Gomel', 'country_id': Country.pick.with_name('Belarus').id},
            {'name': 'Mogilev', 'country_id': Country.pick.with_name('Belarus').id},
            {'name': 'Vitebsk', 'country_id': Country.pick.with_name('Belarus').id},
            {'name': 'Hrodna', 'country_id': Country.pick.with_name('Belarus').id},
            {'name': 'Brest', 'country_id': Country.pick.with_name('Belarus').id},

            {'name': 'Brussels', 'country_id': Country.pick.with_name('Belgium').id},
            {'name': 'Antwerp', 'country_id': Country.pick.with_name('Belgium').id},
            {'name': 'Ghent', 'country_id': Country.pick.with_name('Belgium').id},
            {'name': 'Charleroi', 'country_id': Country.pick.with_name('Belgium').id},
            {'name': 'Liège', 'country_id': Country.pick.with_name('Belgium').id},
            {'name': 'Bruges', 'country_id': Country.pick.with_name('Belgium').id},

            {'name': 'Belmopan', 'country_id': Country.pick.with_name('Belize').id},
            {'name': 'Belize City', 'country_id': Country.pick.with_name('Belize').id},
            {'name': 'San Ignacio', 'country_id': Country.pick.with_name('Belize').id},
            {'name': 'Orange Walk', 'country_id': Country.pick.with_name('Belize').id},
            {'name': 'Dangriga', 'country_id': Country.pick.with_name('Belize').id},
            {'name': 'Corozal', 'country_id': Country.pick.with_name('Belize').id},

            {'name': 'Porto-Novo', 'country_id': Country.pick.with_name('Benin').id},
            {'name': 'Cotonou', 'country_id': Country.pick.with_name('Benin').id},
            {'name': 'Parakou', 'country_id': Country.pick.with_name('Benin').id},
            {'name': 'Djougou', 'country_id': Country.pick.with_name('Benin').id},
            {'name': 'Bohicon', 'country_id': Country.pick.with_name('Benin').id},
            {'name': 'Kandi', 'country_id': Country.pick.with_name('Benin').id},
            
            {'name': 'Parakou', 'country_id': Country.pick.with_name('Benin').id},
            {'name': 'Djougou', 'country_id': Country.pick.with_name('Benin').id},
            {'name': 'Bohicon', 'country_id': Country.pick.with_name('Benin').id},
            {'name': 'Kandi', 'country_id': Country.pick.with_name('Benin').id},
            {'name': 'Save', 'country_id': Country.pick.with_name('Benin').id},
            {'name': 'Nikki', 'country_id': Country.pick.with_name('Benin').id},

            {'name': 'La Paz', 'country_id': Country.pick.with_name('Bolivia').id},
            {'name': 'Sucre', 'country_id': Country.pick.with_name('Bolivia').id},
            {'name': 'Santa Cruz de la Sierra', 'country_id': Country.pick.with_name('Bolivia').id},
            {'name': 'Cochabamba', 'country_id': Country.pick.with_name('Bolivia').id},
            {'name': 'Oruro', 'country_id': Country.pick.with_name('Bolivia').id},
            {'name': 'Tarija', 'country_id': Country.pick.with_name('Bolivia').id},

            {'name': 'Sarajevo', 'country_id': Country.pick.with_name('Bosnia and Herzegovina').id},
            {'name': 'Banja Luka', 'country_id': Country.pick.with_name('Bosnia and Herzegovina').id},
            {'name': 'Tuzla', 'country_id': Country.pick.with_name('Bosnia and Herzegovina').id},
            {'name': 'Zenica', 'country_id': Country.pick.with_name('Bosnia and Herzegovina').id},
            {'name': 'Mostar', 'country_id': Country.pick.with_name('Bosnia and Herzegovina').id},
            {'name': 'Bijeljina', 'country_id': Country.pick.with_name('Bosnia and Herzegovina').id},

            {'name': 'Gaborone', 'country_id': Country.pick.with_name('Botswana').id},
            {'name': 'Francistown', 'country_id': Country.pick.with_name('Botswana').id},
            {'name': 'Molepolole', 'country_id': Country.pick.with_name('Botswana').id},
            {'name': 'Serowe', 'country_id': Country.pick.with_name('Botswana').id},
            {'name': 'Selebi-Phikwe', 'country_id': Country.pick.with_name('Botswana').id},
            {'name': 'Maun', 'country_id': Country.pick.with_name('Botswana').id},

            {'name': 'Brasília', 'country_id': Country.pick.with_name('Brazil').id},
            {'name': 'São Paulo', 'country_id': Country.pick.with_name('Brazil').id},
            {'name': 'Rio de Janeiro', 'country_id': Country.pick.with_name('Brazil').id},
            {'name': 'Salvador', 'country_id': Country.pick.with_name('Brazil').id},
            {'name': 'Fortaleza', 'country_id': Country.pick.with_name('Brazil').id},
            {'name': 'Belo Horizonte', 'country_id': Country.pick.with_name('Brazil').id},

            {'name': 'Sofia', 'country_id': Country.pick.with_name('Bulgaria').id},
            {'name': 'Plovdiv', 'country_id': Country.pick.with_name('Bulgaria').id},
            {'name': 'Varna', 'country_id': Country.pick.with_name('Bulgaria').id},
            {'name': 'Burgas', 'country_id': Country.pick.with_name('Bulgaria').id},
            {'name': 'Ruse', 'country_id': Country.pick.with_name('Bulgaria').id},
            {'name': 'Stara Zagora', 'country_id': Country.pick.with_name('Bulgaria').id},
            {'name': 'Pleven', 'country_id': Country.pick.with_name('Bulgaria').id},

            {'name': 'Ouagadougou', 'country_id': Country.pick.with_name('Burkina Faso').id},
            {'name': 'Bobo-Dioulasso', 'country_id': Country.pick.with_name('Burkina Faso').id},
            {'name': 'Koudougou', 'country_id': Country.pick.with_name('Burkina Faso').id},
            {'name': 'Ouahigouya', 'country_id': Country.pick.with_name('Burkina Faso').id},
            {'name': 'Banfora', 'country_id': Country.pick.with_name('Burkina Faso').id},
            {'name': 'Dédougou', 'country_id': Country.pick.with_name('Burkina Faso').id},

            {'name': 'Bujumbura', 'country_id': Country.pick.with_name('Burundi').id},
            {'name': 'Muyinga', 'country_id': Country.pick.with_name('Burundi').id},
            {'name': 'Ruyigi', 'country_id': Country.pick.with_name('Burundi').id},
            {'name': 'Gitega', 'country_id': Country.pick.with_name('Burundi').id},
            {'name': 'Ngozi', 'country_id': Country.pick.with_name('Burundi').id},
            {'name': 'Bururi', 'country_id': Country.pick.with_name('Burundi').id},
            
            {'name': 'Praia', 'country_id': Country.pick.with_name('Cabo Verde').id},
            {'name': 'Mindelo', 'country_id': Country.pick.with_name('Cabo Verde').id},

            {'name': 'Phnom Penh', 'country_id': Country.pick.with_name('Cambodia').id},
            {'name': 'Siem Reap', 'country_id': Country.pick.with_name('Cambodia').id},

            {'name': 'Yaoundé', 'country_id': Country.pick.with_name('Cameroon').id},
            {'name': 'Douala', 'country_id': Country.pick.with_name('Cameroon').id},

            {'name': 'Ottawa', 'country_id': Country.pick.with_name('Canada').id},
            {'name': 'Toronto', 'country_id': Country.pick.with_name('Canada').id},

            {'name': 'Bangui', 'country_id': Country.pick.with_name('Central African Republic').id},
            {'name': 'Bimbo', 'country_id': Country.pick.with_name('Central African Republic').id},

            {'name': 'N\'Djamena', 'country_id': Country.pick.with_name('Chad').id},
            {'name': 'Moundou', 'country_id': Country.pick.with_name('Chad').id},

            {'name': 'Santiago', 'country_id': Country.pick.with_name('Chile').id},
            {'name': 'São Paulo', 'country_id': Country.pick.with_name('Chile').id},

            {'name': 'Beijing', 'country_id': Country.pick.with_name('China').id},
            {'name': 'Shanghai', 'country_id': Country.pick.with_name('China').id},

            {'name': 'Bogotá', 'country_id': Country.pick.with_name('Colombia').id},
            {'name': 'Medellín', 'country_id': Country.pick.with_name('Colombia').id},

            {'name': 'Moroni', 'country_id': Country.pick.with_name('Comoros').id},
            {'name': 'Mutsamudu', 'country_id': Country.pick.with_name('Comoros').id},

            {'name': 'Brazzaville', 'country_id': Country.pick.with_name('Congo').id},
            {'name': 'Pointe-Noire', 'country_id': Country.pick.with_name('Congo').id},

            {'name': 'San José', 'country_id': Country.pick.with_name('Costa Rica').id},
            {'name': 'Limón', 'country_id': Country.pick.with_name('Costa Rica').id},

            {'name': 'Zagreb', 'country_id': Country.pick.with_name('Croatia').id},
            {'name': 'Split', 'country_id': Country.pick.with_name('Croatia').id},

            {'name': 'Havana', 'country_id': Country.pick.with_name('Cuba').id},
            {'name': 'Santiago de Cuba', 'country_id': Country.pick.with_name('Cuba').id},

            {'name': 'Nicosia', 'country_id': Country.pick.with_name('Cyprus').id},
            {'name': 'Limassol', 'country_id': Country.pick.with_name('Cyprus').id},

            {'name': 'Prague', 'country_id': Country.pick.with_name('Czech Republic').id},
            {'name': 'Brno', 'country_id': Country.pick.with_name('Czech Republic').id},

            {'name': 'Pyongyang', 'country_id': Country.pick.with_name('North Korea').id},
            {'name': 'Hamhung', 'country_id': Country.pick.with_name('North Korea').id},

            {'name': 'Kinshasa', 'country_id': Country.pick.with_name('Democratic Republic of the Congo').id},
            {'name': 'Lubumbashi', 'country_id': Country.pick.with_name('Democratic Republic of the Congo').id},

            {'name': 'Copenhagen', 'country_id': Country.pick.with_name('Denmark').id},
            {'name': 'Aarhus', 'country_id': Country.pick.with_name('Denmark').id},

            {'name': 'Djibouti City', 'country_id': Country.pick.with_name('Djibouti').id},
            {'name': 'Tadjoura', 'country_id': Country.pick.with_name('Djibouti').id},

            {'name': 'Roseau', 'country_id': Country.pick.with_name('Dominica').id},
            {'name': 'Portsmouth', 'country_id': Country.pick.with_name('Dominica').id},

            {'name': 'Santo Domingo', 'country_id': Country.pick.with_name('Dominican Republic').id},
            {'name': 'Santiago', 'country_id': Country.pick.with_name('Dominican Republic').id},

            {'name': 'Dili', 'country_id': Country.pick.with_name('East Timor').id},
            {'name': 'Baucau', 'country_id': Country.pick.with_name('East Timor').id},

            {'name': 'Quito', 'country_id': Country.pick.with_name('Ecuador').id},
            {'name': 'Guayaquil', 'country_id': Country.pick.with_name('Ecuador').id},

            {'name': 'Cairo', 'country_id': Country.pick.with_name('Egypt').id},
            {'name': 'Alexandria', 'country_id': Country.pick.with_name('Egypt').id},

            {'name': 'San Salvador', 'country_id': Country.pick.with_name('El Salvador').id},
            {'name': 'Santa Ana', 'country_id': Country.pick.with_name('El Salvador').id},

            {'name': 'Malabo', 'country_id': Country.pick.with_name('Equatorial Guinea').id},
            {'name': 'Bata', 'country_id': Country.pick.with_name('Equatorial Guinea').id},

            {'name': 'Asmara', 'country_id': Country.pick.with_name('Eritrea').id},
            {'name': 'Keren', 'country_id': Country.pick.with_name('Eritrea').id},

            {'name': 'Tallinn', 'country_id': Country.pick.with_name('Estonia').id},
            {'name': 'Tartu', 'country_id': Country.pick.with_name('Estonia').id},

            {'name': 'Mbabane', 'country_id': Country.pick.with_name('Eswatini').id},
            {'name': 'Manzini', 'country_id': Country.pick.with_name('Eswatini').id},

            {'name': 'Addis Ababa', 'country_id': Country.pick.with_name('Ethiopia').id},
            {'name': 'Dire Dawa', 'country_id': Country.pick.with_name('Ethiopia').id},

            {'name': 'Suva', 'country_id': Country.pick.with_name('Fiji').id},
            {'name': 'Nadi', 'country_id': Country.pick.with_name('Fiji').id},

            {'name': 'Helsinki', 'country_id': Country.pick.with_name('Finland').id},
            {'name': 'Tampere', 'country_id': Country.pick.with_name('Finland').id},

            {'name': 'Paris', 'country_id': Country.pick.with_name('France').id},
            {'name': 'Marseille', 'country_id': Country.pick.with_name('France').id},

            {'name': 'Libreville', 'country_id': Country.pick.with_name('Gabon').id},
            {'name': 'Port-Gentil', 'country_id': Country.pick.with_name('Gabon').id},

            {'name': 'Banjul', 'country_id': Country.pick.with_name('Gambia').id},
            {'name': 'Brikama', 'country_id': Country.pick.with_name('Gambia').id},
            {'name': 'Tbilisi', 'country_id': Country.pick.with_name('Georgia').id},
            {'name': 'Kutaisi', 'country_id': Country.pick.with_name('Georgia').id},

            {'name': 'Berlin', 'country_id': Country.pick.with_name('Germany').id},
            {'name': 'Hamburg', 'country_id': Country.pick.with_name('Germany').id},

            {'name': 'Accra', 'country_id': Country.pick.with_name('Ghana').id},
            {'name': 'Kumasi', 'country_id': Country.pick.with_name('Ghana').id},

            {'name': 'Athens', 'country_id': Country.pick.with_name('Greece').id},
            {'name': 'Thessaloniki', 'country_id': Country.pick.with_name('Greece').id},

            {'name': 'St. George\'s', 'country_id': Country.pick.with_name('Grenada').id},
            {'name': 'Gouyave', 'country_id': Country.pick.with_name('Grenada').id},

            {'name': 'Guatemala City', 'country_id': Country.pick.with_name('Guatemala').id},
            {'name': 'Mixco', 'country_id': Country.pick.with_name('Guatemala').id},

            {'name': 'Conakry', 'country_id': Country.pick.with_name('Guinea').id},
            {'name': 'Nzérékoré', 'country_id': Country.pick.with_name('Guinea').id},

            {'name': 'Bissau', 'country_id': Country.pick.with_name('Guinea-Bissau').id},
            {'name': 'Bafatá', 'country_id': Country.pick.with_name('Guinea-Bissau').id},

            {'name': 'Georgetown', 'country_id': Country.pick.with_name('Guyana').id},
            {'name': 'Linden', 'country_id': Country.pick.with_name('Guyana').id},

            {'name': 'Port-au-Prince', 'country_id': Country.pick.with_name('Haiti').id},
            {'name': 'Cap-Haïtien', 'country_id': Country.pick.with_name('Haiti').id},

            {'name': 'Tegucigalpa', 'country_id': Country.pick.with_name('Honduras').id},
            {'name': 'San Pedro Sula', 'country_id': Country.pick.with_name('Honduras').id},

            {'name': 'Budapest', 'country_id': Country.pick.with_name('Hungary').id},
            {'name': 'Debrecen', 'country_id': Country.pick.with_name('Hungary').id},

            {'name': 'Reykjavik', 'country_id': Country.pick.with_name('Iceland').id},
            {'name': 'Kópavogur', 'country_id': Country.pick.with_name('Iceland').id},

            {'name': 'New Delhi', 'country_id': Country.pick.with_name('India').id},
            {'name': 'Mumbai', 'country_id': Country.pick.with_name('India').id},

            {'name': 'Jakarta', 'country_id': Country.pick.with_name('Indonesia').id},
            {'name': 'Surabaya', 'country_id': Country.pick.with_name('Indonesia').id},

            {'name': 'Tehran', 'country_id': Country.pick.with_name('Iran').id},
            {'name': 'Mashhad', 'country_id': Country.pick.with_name('Iran').id},

            {'name': 'Baghdad', 'country_id': Country.pick.with_name('Iraq').id},
            {'name': 'Basra', 'country_id': Country.pick.with_name('Iraq').id},

            {'name': 'Dublin', 'country_id': Country.pick.with_name('Ireland').id},
            {'name': 'Cork', 'country_id': Country.pick.with_name('Ireland').id},

            {'name': 'Jerusalem', 'country_id': Country.pick.with_name('Israel').id},
            {'name': 'Tel Aviv', 'country_id': Country.pick.with_name('Israel').id},

            {'name': 'Rome', 'country_id': Country.pick.with_name('Italy').id},
            {'name': 'Milan', 'country_id': Country.pick.with_name('Italy').id},

            {'name': 'Yamoussoukro', 'country_id': Country.pick.with_name('Ivory Coast').id},
            {'name': 'Abidjan', 'country_id': Country.pick.with_name('Ivory Coast').id},

            {'name': 'Kingston', 'country_id': Country.pick.with_name('Jamaica').id},
            {'name': 'Montego Bay', 'country_id': Country.pick.with_name('Jamaica').id},

            {'name': 'Tokyo', 'country_id': Country.pick.with_name('Japan').id},
            {'name': 'Yokohama', 'country_id': Country.pick.with_name('Japan').id},

            {'name': 'Amman', 'country_id': Country.pick.with_name('Jordan').id},
            {'name': 'Zarqa', 'country_id': Country.pick.with_name('Jordan').id},

            {'name': 'Nur-Sultan', 'country_id': Country.pick.with_name('Kazakhstan').id},
            {'name': 'Almaty', 'country_id': Country.pick.with_name('Kazakhstan').id},

            {'name': 'Nairobi', 'country_id': Country.pick.with_name('Kenya').id},
            {'name': 'Mombasa', 'country_id': Country.pick.with_name('Kenya').id},

            {'name': 'Tarawa', 'country_id': Country.pick.with_name('Kiribati').id},
            {'name': 'Bairiki', 'country_id': Country.pick.with_name('Kiribati').id},

            {'name': 'Kuwait City', 'country_id': Country.pick.with_name('Kuwait').id},
            {'name': 'Hawalli', 'country_id': Country.pick.with_name('Kuwait').id},

            {'name': 'Bishkek', 'country_id': Country.pick.with_name('Kyrgyzstan').id},
            {'name': 'Osh', 'country_id': Country.pick.with_name('Kyrgyzstan').id},

            {'name': 'Vientiane', 'country_id': Country.pick.with_name('Laos').id},
            {'name': 'Pakse', 'country_id': Country.pick.with_name('Laos').id},

            {'name': 'Riga', 'country_id': Country.pick.with_name('Latvia').id},
            {'name': 'Daugavpils', 'country_id': Country.pick.with_name('Latvia').id},

            {'name': 'Beirut', 'country_id': Country.pick.with_name('Lebanon').id},
            {'name': 'Tripoli', 'country_id': Country.pick.with_name('Lebanon').id},

            {'name': 'Maseru', 'country_id': Country.pick.with_name('Lesotho').id},
            
                {'name': 'Monrovia', 'country_id': Country.pick.with_name('Liberia').id},
            {'name': 'Gbarnga', 'country_id': Country.pick.with_name('Liberia').id},

            {'name': 'Tripoli', 'country_id': Country.pick.with_name('Libya').id},
            {'name': 'Benghazi', 'country_id': Country.pick.with_name('Libya').id},

            {'name': 'Vaduz', 'country_id': Country.pick.with_name('Liechtenstein').id},
            {'name': 'Schaan', 'country_id': Country.pick.with_name('Liechtenstein').id},

            {'name': 'Vilnius', 'country_id': Country.pick.with_name('Lithuania').id},
            {'name': 'Kaunas', 'country_id': Country.pick.with_name('Lithuania').id},

            {'name': 'Luxembourg City', 'country_id': Country.pick.with_name('Luxembourg').id},
            {'name': 'Esch-sur-Alzette', 'country_id': Country.pick.with_name('Luxembourg').id},

            {'name': 'Antananarivo', 'country_id': Country.pick.with_name('Madagascar').id},
            {'name': 'Toamasina', 'country_id': Country.pick.with_name('Madagascar').id},

            {'name': 'Lilongwe', 'country_id': Country.pick.with_name('Malawi').id},
            {'name': 'Blantyre', 'country_id': Country.pick.with_name('Malawi').id},

            {'name': 'Kuala Lumpur', 'country_id': Country.pick.with_name('Malaysia').id},
            {'name': 'George Town', 'country_id': Country.pick.with_name('Malaysia').id},

            {'name': 'Malé', 'country_id': Country.pick.with_name('Maldives').id},
            {'name': 'Fuvahmulah', 'country_id': Country.pick.with_name('Maldives').id},

            {'name': 'Bamako', 'country_id': Country.pick.with_name('Mali').id},
            {'name': 'Sikasso', 'country_id': Country.pick.with_name('Mali').id},

            {'name': 'Valletta', 'country_id': Country.pick.with_name('Malta').id},
            {'name': 'Birkirkara', 'country_id': Country.pick.with_name('Malta').id},

            {'name': 'Majuro', 'country_id': Country.pick.with_name('Marshall Islands').id},
            {'name': 'Ebeye', 'country_id': Country.pick.with_name('Marshall Islands').id},

            {'name': 'Nouakchott', 'country_id': Country.pick.with_name('Mauritania').id},
            {'name': 'Nouadhibou', 'country_id': Country.pick.with_name('Mauritania').id},

            {'name': 'Port Louis', 'country_id': Country.pick.with_name('Mauritius').id},
            {'name': 'Beau Bassin-Rose Hill', 'country_id': Country.pick.with_name('Mauritius').id},

            {'name': 'Mexico City', 'country_id': Country.pick.with_name('Mexico').id},
            {'name': 'Guadalajara', 'country_id': Country.pick.with_name('Mexico').id},

            {'name': 'Palikir', 'country_id': Country.pick.with_name('Micronesia').id},
            {'name': 'Weno', 'country_id': Country.pick.with_name('Micronesia').id},

            {'name': 'Chișinău', 'country_id': Country.pick.with_name('Moldova').id},
            {'name': 'Bălți', 'country_id': Country.pick.with_name('Moldova').id},

            {'name': 'Monaco', 'country_id': Country.pick.with_name('Monaco').id},
            {'name': 'Monte Carlo', 'country_id': Country.pick.with_name('Monaco').id},

            {'name': 'Ulaanbaatar', 'country_id': Country.pick.with_name('Mongolia').id},
            {'name': 'Erdenet', 'country_id': Country.pick.with_name('Mongolia').id},

            {'name': 'Podgorica', 'country_id': Country.pick.with_name('Montenegro').id},
            {'name': 'Nikšić', 'country_id': Country.pick.with_name('Montenegro').id},

            {'name': 'Rabat', 'country_id': Country.pick.with_name('Morocco').id},
            {'name': 'Casablanca', 'country_id': Country.pick.with_name('Morocco').id},

            {'name': 'Maputo', 'country_id': Country.pick.with_name('Mozambique').id},
            {'name': 'Matola', 'country_id': Country.pick.with_name('Mozambique').id},

            {'name': 'Naypyidaw', 'country_id': Country.pick.with_name('Myanmar').id},
            {'name': 'Yangon', 'country_id': Country.pick.with_name('Myanmar').id},

            {'name': 'Windhoek', 'country_id': Country.pick.with_name('Namibia').id},

            {'name': 'Nauru', 'country_id': Country.pick.with_name('Nauru').id},
            {'name': 'Yaren', 'country_id': Country.pick.with_name('Nauru').id},

            {'name': 'Kathmandu', 'country_id': Country.pick.with_name('Nepal').id},
            {'name': 'Pokhara', 'country_id': Country.pick.with_name('Nepal').id},

            {'name': 'Amsterdam', 'country_id': Country.pick.with_name('Netherlands').id},
            {'name': 'Rotterdam', 'country_id': Country.pick.with_name('Netherlands').id},

            {'name': 'Wellington', 'country_id': Country.pick.with_name('New Zealand').id},
            {'name': 'Auckland', 'country_id': Country.pick.with_name('New Zealand').id},

            {'name': 'Managua', 'country_id': Country.pick.with_name('Nicaragua').id},
            {'name': 'León', 'country_id': Country.pick.with_name('Nicaragua').id},

            {'name': 'Niamey', 'country_id': Country.pick.with_name('Niger').id},
            {'name': 'Zinder', 'country_id': Country.pick.with_name('Niger').id},

            {'name': 'Lagos', 'country_id': Country.pick.with_name('Nigeria').id},
            {'name': 'Kano', 'country_id': Country.pick.with_name('Nigeria').id},

            {'name': 'Skopje', 'country_id': Country.pick.with_name('North Macedonia').id},
            {'name': 'Bitola', 'country_id': Country.pick.with_name('North Macedonia').id},

            {'name': 'Oslo', 'country_id': Country.pick.with_name('Norway').id},
            {'name': 'Bergen', 'country_id': Country.pick.with_name('Norway').id},

            {'name': 'Muscat', 'country_id': Country.pick.with_name('Oman').id},
            {'name': 'Salalah', 'country_id': Country.pick.with_name('Oman').id},

            {'name': 'Islamabad', 'country_id': Country.pick.with_name('Pakistan').id},
            {'name': 'Karachi', 'country_id': Country.pick.with_name('Pakistan').id},

            {'name': 'Ngerulmud', 'country_id': Country.pick.with_name('Palau').id},
            {'name': 'Koror', 'country_id': Country.pick.with_name('Palau').id},

            {'name': 'East Jerusalem', 'country_id': Country.pick.with_name('Palestine').id},
            {'name': 'Gaza City', 'country_id': Country.pick.with_name('Palestine').id},

            {'name': 'Panama City', 'country_id': Country.pick.with_name('Panama').id},
            {'name': 'San Miguelito', 'country_id': Country.pick.with_name('Panama').id},

            {'name': 'Port Moresby', 'country_id': Country.pick.with_name('Papua New Guinea').id},
            {'name': 'Lae', 'country_id': Country.pick.with_name('Papua New Guinea').id},

            {'name': 'Asunción', 'country_id': Country.pick.with_name('Paraguay').id},
            {'name': 'Ciudad del Este', 'country_id': Country.pick.with_name('Paraguay').id},

            {'name': 'Lima', 'country_id': Country.pick.with_name('Peru').id},
            {'name': 'Arequipa', 'country_id': Country.pick.with_name('Peru').id},

            {'name': 'Manila', 'country_id': Country.pick.with_name('Philippines').id},
            {'name': 'Quezon City', 'country_id': Country.pick.with_name('Philippines').id},

            {'name': 'Warsaw', 'country_id': Country.pick.with_name('Poland').id},
            {'name': 'Kraków', 'country_id': Country.pick.with_name('Poland').id},

            {'name': 'Lisbon', 'country_id': Country.pick.with_name('Portugal').id},
            {'name': 'Porto', 'country_id': Country.pick.with_name('Portugal').id},

            {'name': 'Doha', 'country_id': Country.pick.with_name('Qatar').id},
            {'name': 'Al Wakrah', 'country_id': Country.pick.with_name('Qatar').id},

            {'name': 'Bucharest', 'country_id': Country.pick.with_name('Romania').id},
            {'name': 'Cluj-Napoca', 'country_id': Country.pick.with_name('Romania').id},

            {'name': 'Moscow', 'country_id': Country.pick.with_name('Russia').id},
            {'name': 'Saint Petersburg', 'country_id': Country.pick.with_name('Russia').id},
            {"name": "Novosibirsk", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Yekaterinburg", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Nizhny Novgorod", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Kazan", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Chelyabinsk", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Omsk", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Samara", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Rostov-on-Don", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Ufa", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Krasnoyarsk", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Perm", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Voronezh", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Volgograd", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Saratov", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Krasnodar", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Tolyatti", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Izhevsk", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Yaroslavl", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Barnaul", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Vladivostok", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Irkutsk", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Khabarovsk", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Kemerovo", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Novokuznetsk", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Orenburg", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Ryazan", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Tomsk", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Astrakhan", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Penza", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Lipetsk", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Tula", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Kurgan", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Ivanovo", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Ulan-Ude", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Bryansk", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Kursk", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Tver", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Magnitogorsk", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Kaliningrad", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Belgorod", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Nizhnevartovsk", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Smolensk", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Kaluga", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Chita", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Kostroma", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Orel", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Volzhsky", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Novorossiysk", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Taganrog", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Norilsk", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Zheleznogorsk", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Vologda", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Sterlitamak", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Angarsk", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Blagoveshchensk", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Yuzhno-Sakhalinsk", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Veliky Novgorod", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Nalchik", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Cherepovets", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Huelva", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Lipeck", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Abakan", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Barnaul", "country_id": Country.pick.with_name("Russia").id},
            {"name": "Belgorod", "country_id": Country.pick.with_name("Russia").id},

            {'name': 'Kigali', 'country_id': Country.pick.with_name('Rwanda').id},
            {'name': 'Butare', 'country_id': Country.pick.with_name('Rwanda').id},

            {'name': 'Basseterre', 'country_id': Country.pick.with_name('Saint Kitts and Nevis').id},
            {'name': 'Charlestown', 'country_id': Country.pick.with_name('Saint Kitts and Nevis').id},

            {'name': 'Castries', 'country_id': Country.pick.with_name('Saint Lucia').id},
            {'name': 'Vieux Fort', 'country_id': Country.pick.with_name('Saint Lucia').id},

            {'name': 'Kingstown', 'country_id': Country.pick.with_name('Saint Vincent and the Grenadines').id},
            {'name': 'Arnos Vale', 'country_id': Country.pick.with_name('Saint Vincent and the Grenadines').id},

            {'name': 'Apia', 'country_id': Country.pick.with_name('Samoa').id},
            {'name': 'Vaitele', 'country_id': Country.pick.with_name('Samoa').id},

            {'name': 'San Marino', 'country_id': Country.pick.with_name('San Marino').id},
            {'name': 'Serravalle', 'country_id': Country.pick.with_name('San Marino').id},

            {'name': 'São Tomé', 'country_id': Country.pick.with_name('Sao Tome and Principe').id},
            {'name': 'Trindade', 'country_id': Country.pick.with_name('Sao Tome and Principe').id},

            {'name': 'Riyadh', 'country_id': Country.pick.with_name('Saudi Arabia').id},
            {'name': 'Jeddah', 'country_id': Country.pick.with_name('Saudi Arabia').id},

            {'name': 'Dakar', 'country_id': Country.pick.with_name('Senegal').id},
            {'name': 'Grand Dakar', 'country_id': Country.pick.with_name('Senegal').id},

            {'name': 'Belgrade', 'country_id': Country.pick.with_name('Serbia').id},
            
            {'name': 'Victoria', 'country_id': Country.pick.with_name('Seychelles').id},
            {'name': 'Anse Royale', 'country_id': Country.pick.with_name('Seychelles').id},

            {'name': 'Freetown', 'country_id': Country.pick.with_name('Sierra Leone').id},
            {'name': 'Bo', 'country_id': Country.pick.with_name('Sierra Leone').id},

            {'name': 'Singapore', 'country_id': Country.pick.with_name('Singapore').id},
            {'name': 'Woodlands', 'country_id': Country.pick.with_name('Singapore').id},

            {'name': 'Bratislava', 'country_id': Country.pick.with_name('Slovakia').id},
            {'name': 'Košice', 'country_id': Country.pick.with_name('Slovakia').id},

            {'name': 'Ljubljana', 'country_id': Country.pick.with_name('Slovenia').id},
            {'name': 'Maribor', 'country_id': Country.pick.with_name('Slovenia').id},

            {'name': 'Honiara', 'country_id': Country.pick.with_name('Solomon Islands').id},
            {'name': 'Gizo', 'country_id': Country.pick.with_name('Solomon Islands').id},

            {'name': 'Mogadishu', 'country_id': Country.pick.with_name('Somalia').id},
            {'name': 'Hargeisa', 'country_id': Country.pick.with_name('Somalia').id},

            {'name': 'Pretoria', 'country_id': Country.pick.with_name('South Africa').id},
            {'name': 'Johannesburg', 'country_id': Country.pick.with_name('South Africa').id},

            {'name': 'Seoul', 'country_id': Country.pick.with_name('South Korea').id},
            {'name': 'Busan', 'country_id': Country.pick.with_name('South Korea').id},

            {'name': 'Juba', 'country_id': Country.pick.with_name('South Sudan').id},
            {'name': 'Malakal', 'country_id': Country.pick.with_name('South Sudan').id},

            {'name': 'Madrid', 'country_id': Country.pick.with_name('Spain').id},
            {'name': 'Barcelona', 'country_id': Country.pick.with_name('Spain').id},

            {'name': 'Colombo', 'country_id': Country.pick.with_name('Sri Lanka').id},
            {'name': 'Galkissa', 'country_id': Country.pick.with_name('Sri Lanka').id},

            {'name': 'Khartoum', 'country_id': Country.pick.with_name('Sudan').id},
            {'name': 'Omdurman', 'country_id': Country.pick.with_name('Sudan').id},

            {'name': 'Paramaribo', 'country_id': Country.pick.with_name('Suriname').id},
            {'name': 'Lelydorp', 'country_id': Country.pick.with_name('Suriname').id},

            {'name': 'Stockholm', 'country_id': Country.pick.with_name('Sweden').id},
            {'name': 'Gothenburg', 'country_id': Country.pick.with_name('Sweden').id},

            {'name': 'Bern', 'country_id': Country.pick.with_name('Switzerland').id},
            {'name': 'Zurich', 'country_id': Country.pick.with_name('Switzerland').id},

            {'name': 'Damascus', 'country_id': Country.pick.with_name('Syria').id},
            {'name': 'Aleppo', 'country_id': Country.pick.with_name('Syria').id},

            {'name': 'Taipei', 'country_id': Country.pick.with_name('Taiwan').id},
            {'name': 'Kaohsiung', 'country_id': Country.pick.with_name('Taiwan').id},

            {'name': 'Dushanbe', 'country_id': Country.pick.with_name('Tajikistan').id},
            {'name': 'Khujand', 'country_id': Country.pick.with_name('Tajikistan').id},

            {'name': 'Dodoma', 'country_id': Country.pick.with_name('Tanzania').id},
            {'name': 'Dar es Salaam', 'country_id': Country.pick.with_name('Tanzania').id},

            {'name': 'Bangkok', 'country_id': Country.pick.with_name('Thailand').id},
            {'name': 'Nakhon Ratchasima', 'country_id': Country.pick.with_name('Thailand').id},

            {'name': 'Lomé', 'country_id': Country.pick.with_name('Togo').id},
            {'name': 'Sokodé', 'country_id': Country.pick.with_name('Togo').id},

            {'name': 'Nukuʻalofa', 'country_id': Country.pick.with_name('Tonga').id},
            {'name': 'Haveluloto', 'country_id': Country.pick.with_name('Tonga').id},

            {'name': 'Port of Spain', 'country_id': Country.pick.with_name('Trinidad and Tobago').id},
            {'name': 'Chaguanas', 'country_id': Country.pick.with_name('Trinidad and Tobago').id},

            {'name': 'Tunis', 'country_id': Country.pick.with_name('Tunisia').id},
            {'name': 'Sfax', 'country_id': Country.pick.with_name('Tunisia').id},

            {'name': 'Ankara', 'country_id': Country.pick.with_name('Turkey').id},
            {'name': 'Istanbul', 'country_id': Country.pick.with_name('Turkey').id},

            {'name': 'Ashgabat', 'country_id': Country.pick.with_name('Turkmenistan').id},
            {'name': 'Turkmenabat', 'country_id': Country.pick.with_name('Turkmenistan').id},

            {'name': 'Funafuti', 'country_id': Country.pick.with_name('Tuvalu').id},
            {'name': 'Vaiaku', 'country_id': Country.pick.with_name('Tuvalu').id},

            {'name': 'Kampala', 'country_id': Country.pick.with_name('Uganda').id},
            {'name': 'Gulu', 'country_id': Country.pick.with_name('Uganda').id},

            {'name': 'Kiev', 'country_id': Country.pick.with_name('Ukraine').id},
            {'name': 'Kharkiv', 'country_id': Country.pick.with_name('Ukraine').id},

            {'name': 'Abu Dhabi', 'country_id': Country.pick.with_name('United Arab Emirates').id},
            {'name': 'Dubai', 'country_id': Country.pick.with_name('United Arab Emirates').id},

            {'name': 'Edinburgh', 'country_id': Country.pick.with_name('United Kingdom').id},
            {'name': 'Manchester', 'country_id': Country.pick.with_name('United Kingdom').id},

            {'name': 'Washington, D.C.', 'country_id': Country.pick.with_name('United States of America').id},
            {'name': 'New York City', 'country_id': Country.pick.with_name('United States of America').id},
            {'name': 'Los Angeles', 'country_id': Country.pick.with_name('United States of America').id},

            {'name': 'Montevideo', 'country_id': Country.pick.with_name('Uruguay').id},
            {'name': 'Salto', 'country_id': Country.pick.with_name('Uruguay').id},

            {'name': 'Tashkent', 'country_id': Country.pick.with_name('Uzbekistan').id},
            {'name': 'Namangan', 'country_id': Country.pick.with_name('Uzbekistan').id},

            {'name': 'Port Vila', 'country_id': Country.pick.with_name('Vanuatu').id},
            {'name': 'Luganville', 'country_id': Country.pick.with_name('Vanuatu').id},

            {'name': 'Vatican City', 'country_id': Country.pick.with_name('Vatican City').id},
            {'name': 'Gardens of Vatican City', 'country_id': Country.pick.with_name('Vatican City').id},

            {'name': 'Caracas', 'country_id': Country.pick.with_name('Venezuela').id},
            {'name': 'Maracaibo', 'country_id': Country.pick.with_name('Venezuela').id},

            {'name': 'Hanoi', 'country_id': Country.pick.with_name('Vietnam').id},
            {'name': 'Ho Chi Minh City', 'country_id': Country.pick.with_name('Vietnam').id},

            {'name': 'Sanaa', 'country_id': Country.pick.with_name('Yemen').id},
            {'name': 'Aden', 'country_id': Country.pick.with_name('Yemen').id},

            {'name': 'Lusaka', 'country_id': Country.pick.with_name('Zambia').id},
            {'name': 'Ndola', 'country_id': Country.pick.with_name('Zambia').id},

            {'name': 'Harare', 'country_id': Country.pick.with_name('Zimbabwe').id},
            {'name': 'Bulawayo', 'country_id': Country.pick.with_name('Zimbabwe').id}
        ]