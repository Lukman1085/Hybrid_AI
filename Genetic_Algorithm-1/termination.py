from selection import selection  # pastikan fungsi selection kamu sudah benar

def termination(populasi):
    # Ambil individu terbaik dari populasi
    best_solution, _ = selection(populasi)

    # Jika fitness mencapai target
    if best_solution["fitness"] == 100:
        is_looping = False
        print("Ketemu jawabannya!")
    else:
        is_looping = True

    solusi = best_solution
    return is_looping, solusi
