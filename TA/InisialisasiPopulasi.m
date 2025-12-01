function Populasi = InisialisasiPopulasi(UkPop, JumGen)

for k = 1:UkPop
    for g = 1:JumGen
        a = rand;
        if(a < 0.5)
            Populasi(k,g) = 0;
        else 
            Populasi(k,g) = 1;
        end
    end
end