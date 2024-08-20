# Tested: 2024/08/05
# by Kasper Arfman
name: Build APK
on: [push]
jobs:
  build-android:
    name: Build for Android
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Buildozer dependencies
        run: |
          sudo apt update
          sudo apt install -y git zip unzip python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev automake
          pip install --user --upgrade Cython virtualenv
          pip install --user --upgrade buildozer
          echo 'export PATH=$PATH:~/.local/bin/' >> ~/.bashrc

      - name: Handle Java path
        run: |
          export JAVA_HOME=/usr/lib/jvm/temurin-17-jdk-amd64
          sudo update-java-alternatives --set ${JAVA_HOME}
          export PATH=$JAVA_HOME/bin:$PATH
          yes | buildozer -v android debug

      - name: Upload artifacts
        uses: actions/upload-artifact@v2
        with:
          name: package
          path: bin/*.apk
