fn main() {
    let vendor = buildsupport::vendor_dir();

    let src = vendor.join("src");
    let utf8 = vendor.join("third_party/utf8_range");

    let mut lib = buildsupport::CxxLib::new("protobuf");
    lib.include(&src)
        .include(&utf8)
        // The generated well-known-type classes sit at the vendor root
        // ("google/protobuf/any.pb.h"), outside the src/ include root.
        .include(&vendor)
        .include_deps(&["absl"]);
    lib.files_from_filelist(&vendor);
    lib.compile();
    lib.export();
}
