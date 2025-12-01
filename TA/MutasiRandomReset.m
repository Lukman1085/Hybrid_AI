function MutKrom = MutasiRandomReset(Kromosom, JumGen, Pmutasi)
    MutKrom = Kromosom;
    for ii = 1:JumGen
        if(rand < Pmutasi)
            % LOGIKA RANDOM RESET:
            % Atur ulang nilai menjadi acak 0 atau 1.
            % Fungsi round(rand) atau randi([0,1]) menghasilkan 0 atau 1 secara acak.
            
            MutKrom(ii) = round(rand); 
            
            % Catatan: Ada peluang 50% nilai tetap sama, 
            % tapi inilah definisi "Random Reset".
        end
    end
end