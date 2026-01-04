{ pkgs, ... }: {
  # Kullanılacak paketler
  packages = [
    pkgs.python3
  ];

  # IDX ayarları
  idx = {
    # Kullanılacak VS Code eklentileri
    extensions = [
      "vscodevim.vim" # İsteğe bağlı
    ];

    # Önizleme (Preview) yapılandırması
    previews = {
      enable = true;
      previews = {
        web = {
          # HTML dosyalarını sunmak için basit bir python sunucusu başlatır
          command = ["python3" "-m" "http.server" "$PORT" "--bind" "0.0.0.0"];
          manager = "web";
        };
      };
    };
  };
}
