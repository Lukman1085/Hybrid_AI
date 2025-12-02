function [GenerasiAkhir, FitnessTerbaik] = Copy_of_FFNNBinaryLatih()
    JumMasukan = 3;
    JPmasukan = 2^JumMasukan;
    Nbit = 20;
    JumGen = Nbit*(JumMasukan+1)^2;
    Nvar = JumGen/Nbit;
    Rb = -10;
    Ra = 10;
    MinDelta = 0.01;
    Fthreshold = 1/MinDelta;
    
    
    UkPop = 40;
    Psilang = 0.8;
    Pmutasi = 0.03;
    MaxG = 2000;
    
    
    [IM,TM] = BangMatrixIT(JumMasukan,JPmasukan);
    
    Populasi  = InisialisasiPopulasi(UkPop,JumGen);
    
    Fitness = zeros(1, UkPop);
    
    GenerasiAkhir = MaxG;
    FitnessTerbaik = 0;
    
    for generasi = 1:MaxG
        FFNNstruk = DekodekanKromosom(Populasi(1,:),Nvar,Nbit,Ra,Rb);
        Fitness(1) = BinaryEvalInd(FFNNstruk, JumMasukan, JPmasukan,IM,TM);
        MaxF = Fitness(1);
        MinF = Fitness(1);
        IndeksIndividuTerbaik = 1;
        for ii=2:UkPop
            FFNNstruk = DekodekanKromosom(Populasi(ii,:),Nvar,Nbit,Ra,Rb);
            Fitness(ii) = BinaryEvalInd(FFNNstruk, JumMasukan, JPmasukan,IM,TM);
            if (Fitness(ii) > MaxF)
                MaxF = Fitness(ii);
                IndeksIndividuTerbaik = ii;
            end
            if (Fitness(ii) <= MinF)
                MinF = Fitness(ii);
            end
        end

        [FitnessSorted, IndeksUrut] = sort(Fitness, 'descend');
        Populasi = Populasi(IndeksUrut, :);
        Fitness = FitnessSorted;


        FitnessTerbaik = MaxF;
    
        if MaxF > Fthreshold
            GenerasiAkhir = generasi;
            return;
        end
    
        TemPopulasi = Populasi;
    
        if mod(UkPop,2) == 0
            IterasiMulai = 3;
            TemPopulasi(1,:) = Populasi(IndeksIndividuTerbaik,:);
            TemPopulasi(2,:) = Populasi(IndeksIndividuTerbaik,:);
        else
            IterasiMulai = 2;
            TemPopulasi(1,:) = Populasi(IndeksIndividuTerbaik,:);
        end
    
        for jj = IterasiMulai:2:UkPop
            IP1 = RankSelection(UkPop);
            IP2 = RankSelection(UkPop);
    
            if(rand < Psilang)
                Anak = PindahSilang(Populasi(IP1,:), Populasi(IP2,:), JumGen);
                TemPopulasi(jj,:) = Anak(1,:);
                TemPopulasi(jj+1,:) = Anak(2,:);
            else
                TemPopulasi(jj,:) = Populasi(IP1,:);
                TemPopulasi(jj+1,:) = Populasi(IP2,:);
            end
        end
    
        for kk = IterasiMulai:UkPop
            TemPopulasi(kk,:) = MutasiRandomReset(TemPopulasi(kk,:), JumGen, Pmutasi);
        end
    
        Populasi = TemPopulasi;
    
    end
end



        

